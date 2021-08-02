import sys


class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans


input = sys.stdin.readline

n, m = list(map(int, input().split()))
t = list(map(int, input().split()))
t = [t[i] - 1 for i in range(n)]
query = []
for i in range(m - 1):
    a, b = list(map(int, input().split()))
    query.append((a - 1, b - 1))

tower = [[] for i in range(m)]
for i in range(n):
    id = t[i]
    if not tower[id]:
        tower[id].append((i + 1, i + 1))
    else:
        start, end = tower[id].pop()
        if end + 1 == i + 1:
            tower[id].append((start, i + 1))
        else:
            tower[id].append((start, end))
            tower[id].append((i + 1, i + 1))

# print(tower)
test = []
for i in range(m):
    for start, end in tower[i]:
        if end != n:
            test.append((t[start - 1], t[end]))

# print(test)
start = [-1] * len(test)
end = [m - 1] * len(test)
temp = [[] for i in range(m)]
for i in range(len(test)):
    T = (end[i] + start[i]) // 2
    temp[T].append(i)


def parabisect():
    uf = UnionFindVerSize(m)
    for i in range(m - 1):
        a, b = query[i]
        uf.unite(a, b)
        while temp[i]:
            j = temp[i].pop()
            id1, id2 = test[j]
            if uf.is_same_group(id1, id2):
                end[j] = i
            else:
                start[j] = i
            if end[j] - start[j] > 1:
                T = (end[j] + start[j]) // 2
                temp[T].append(j)


for i in range(20):
    parabisect()

res = [0] * m
for i in range(len(test)):
    res[end[i] + 1] -= 1

for i in range(1, m):
    res[i] += res[i - 1]

for i in range(m):
    print(len(test) + res[i])
