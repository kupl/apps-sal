from bisect import bisect_left, bisect_right
from decimal import Decimal
from scipy.special import comb
n, a, b = map(int, input().split())
v = list(map(lambda x:-int(x), input().split()))
v.sort()
li = [[None]*2 for _ in range(n+1)]
for k in range(a, b+1):
    li[k][0] = -sum(v[:k])
    li[k][1] = comb(bisect_right(v, v[k-1])-bisect_left(v, v[k-1]), k-bisect_left(v, v[k-1]), exact=True)
ans = [Decimal(0), 0]
for i in range(n+1):
    if li[i][0] is None:
        continue
    tmp = Decimal(li[i][0]) / Decimal(i)
    if ans[0]==tmp:
        ans[1] += li[i][1]
    elif ans[0]<tmp:
        ans[0] = tmp
        ans[1] = li[i][1]
print(ans[0])
print(ans[1])
