from collections import defaultdict as dd
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

l = list(map(int, input().split()))
if(m == 1):
    l.sort(reverse=True)
    su = 0
    for i in range(k):
        su += l[i]
    print(su)
    return
pre = [0]
for i in range(n):
    pre.append(pre[-1] + l[i])
dp = dd(int)
mx = dd(int)
for i in range(0, n - m * k + 1):
    dp[(i, 0)] = pre[i + m] - pre[i]
    if(i == 0):
        mx[i] = dp[(i, 0)]
    else:
        mx[i] = max(mx[i - 1], dp[(i, 0)])
# print(mx)
for j in range(1, k):
    mx2 = [0] * n
    for i in range(j * m, n - (k - j) * m + 1):
        dp[(i, j)] = pre[i + m] - pre[i] + mx[i - m]
        if(i == j * m):
            mx2[i] = dp[(i, j)]
        else:
            mx2[i] = max(mx2[i - 1], dp[(i, j)])
    mx = mx2
ans = 0
for i in range(n):
    ans = max(ans, dp[(i, k - 1)])
print(ans)
