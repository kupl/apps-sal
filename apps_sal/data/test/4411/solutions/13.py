from collections import Counter
import sys
from bisect import bisect_right, bisect_left


class BITbisect():
    def __init__(self, InputProbNumbers):
        self.ind_to_co = [-10**18]
        self.co_to_ind = {}
        for ind, num in enumerate(sorted(list(set(InputProbNumbers)))):
            self.ind_to_co.append(num)
            self.co_to_ind[num] = ind + 1
        self.max = len(self.co_to_ind)
        self.data = [0] * (self.max + 1)

    def __str__(self):
        retList = []
        for i in range(1, self.max + 1):
            x = self.ind_to_co[i]
            if self.count(x):
                c = self.count(x)
                for _ in range(c):
                    retList.append(x)
        return "[" + ", ".join([str(a) for a in retList]) + "]"

    def __getitem__(self, key):
        key += 1
        s = 0
        ind = 0
        l = self.max.bit_length()
        for i in reversed(range(l)):
            if ind + (1 << i) <= self.max:
                if s + self.data[ind + (1 << i)] < key:
                    s += self.data[ind + (1 << i)]
                    ind += (1 << i)
        if ind == self.max or key < 0:
            raise IndexError("BIT index out of range")
        return self.ind_to_co[ind + 1]

    def __len__(self):
        return self._query_sum(self.max)

    def __contains__(self, num):
        if not num in self.co_to_ind:
            return False
        return self.count(num) > 0

    def _query_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def _add(self, i, x):
        while i <= self.max:
            self.data[i] += x
            i += i & -i

    def push(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The pushing number didnt initialized")
        self._add(self.co_to_ind[x], 1)

    def delete(self, x):
        if not x in self.co_to_ind:
            raise KeyError("The deleting number didnt initialized")
        if self.count(x) <= 0:
            raise ValueError("The deleting number doesnt exist")
        self._add(self.co_to_ind[x], -1)

    def count(self, x):
        return self._query_sum(self.co_to_ind[x]) - self._query_sum(self.co_to_ind[x] - 1)

    def bisect_right(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_right(self.ind_to_co, x) - 1
        return self._query_sum(i)

    def bisect_left(self, x):
        if x in self.co_to_ind:
            i = self.co_to_ind[x]
        else:
            i = bisect_left(self.ind_to_co, x)
        if i == 1:
            return 0
        return self._query_sum(i - 1)


input = sys.stdin.readline
MAX = 2 * 10**5 + 3

N, K = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(N)]
A = [[] for _ in range(MAX)]
B = BITbisect(list(range(MAX)))
P = [[] for _ in range(MAX)]
for i, (l, r) in enumerate(Query):
    A[l].append(r)
    P[r].append((l, i + 1))

mustL = []
for n in range(MAX):
    for r in A[n]:
        B.push(r)
    while len(B) > 0:
        b = B[0]
        if b < n:
            B.delete(b)
        else:
            break
    l = len(B)
    d = l - K
    if d > 0:
        for _ in range(d):
            b = B[l - 1]
            B.delete(b)
            mustL.append(b)
            l -= 1

C = Counter(mustL)
ans = []
for r, c in C.items():
    P[r].sort()
    for i in range(c):
        ans.append(P[r][i][1])

print(len(ans))
print(*ans)
