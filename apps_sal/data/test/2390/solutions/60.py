from itertools import accumulate

n, c = list(map(int, input().split()))
xv = [[0, 0]] + [list(map(int, input().split())) for i in range(n)]
xv_rev = [[0, 0]] + [[c - x, v] for x, v in xv][:0:-1]
cumsum = [i - x for i, (x, v) in zip(list(accumulate([v for x, v in xv])), xv)]
cumsum_rev = [i - x for i, (x, v) in zip(list(accumulate([v for x, v in xv_rev])), xv_rev)]
xv_max = [0]
xv_rev_max = [0]
now_v = 0
for k, (x, v) in enumerate(xv[:-1], 1):
    xv_max.append(max(xv_max[-1], cumsum[k]))
for k, (x, v) in enumerate(xv_rev[:-1], 1):
    xv_rev_max.append(max(xv_rev_max[-1], cumsum_rev[k]))
ans = 0
for i, j, (x, v) in zip(xv_max, cumsum_rev[::-1], xv_rev[::-1]):
    ans = max(ans, i + j - x)
for i, j, (x, v) in zip(xv_rev_max, cumsum[::-1], xv[::-1]):
    ans = max(ans, i + j - x)
print(ans)
