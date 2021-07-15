# https://codeforces.com/contest/1042/problem/D
# 解説AC
# sr - sl < t
# sl > sr - t
# index - sr -t 以下の数

from itertools import accumulate

class binary_index_tree(object):
    def __init__(self, n):
        self.bit = [0]*n
        self.n = n
    def add(self, ind, num):
        # index is one_indexed
        while(ind <= self.n):
            self.bit[ind - 1] += num
            ind += ind & -ind
    # [1, ind)
    def sum(self, ind):
        # index is one indexed
        ret = 0
        while(ind > 0):
            ret += self.bit[ind-1]
            ind -= ind & -ind
        return ret
    # [from_, to_)
    def sum_from(self, from_, to_):
        # index is one indexed
        return self.sum(to_) - self.sum(from_)

n,t = map(int, input().split())
a = list(map(int, input().split()))
sa = list(accumulate(a))
ss = sa + [i-t for i in sa]
#print(ss)
ss.sort()
# 座圧
d = {}
cnt = 0
for i in sorted(ss):
    if i not in d:
        d[i] = cnt
        cnt += 1
BIT = binary_index_tree(cnt+1)
ans = 0
for ar in sa:
    # 1-indexed
    r = d[ar-t] + 1
    i = d[ar] + 1
    ans += BIT.sum_from(r, cnt+1)
    BIT.add(i, 1)
#print(ans)
for i in sa:
    if i < t:
        ans += 1
print(ans)
