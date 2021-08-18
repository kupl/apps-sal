
from itertools import accumulate


class binary_index_tree(object):
    def __init__(self, n):
        self.bit = [0] * n
        self.n = n

    def add(self, ind, num):
        while(ind <= self.n):
            self.bit[ind - 1] += num
            ind += ind & -ind

    def sum(self, ind):
        ret = 0
        while(ind > 0):
            ret += self.bit[ind - 1]
            ind -= ind & -ind
        return ret

    def sum_from(self, from_, to_):
        return self.sum(to_) - self.sum(from_)


n, t = map(int, input().split())
a = list(map(int, input().split()))
sa = list(accumulate(a))
ss = sa + [i - t for i in sa]
ss.sort()
d = {}
cnt = 0
for i in sorted(ss):
    if i not in d:
        d[i] = cnt
        cnt += 1
BIT = binary_index_tree(cnt + 1)
ans = 0
for ar in sa:
    r = d[ar - t] + 1
    i = d[ar] + 1
    ans += BIT.sum_from(r, cnt + 1)
    BIT.add(i, 1)
for i in sa:
    if i < t:
        ans += 1
print(ans)
