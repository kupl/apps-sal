"""

created by shuangquan.huang at 11/21/18

"""
import bisect
(N, H) = list(map(int, input().split()))
X = []
s = float('inf')
for i in range(N):
    (x1, x2) = list(map(int, input().split()))
    s = min(s, x1)
    X.append((x1, x2))
X = [(x1 - s, x2 - s) for (x1, x2) in X]
X.sort()
gap = [0] * (N + 1)
for i in range(1, N):
    gap[i] = X[i][0] - X[i - 1][1]
gpresum = [0] * (N + 1)
for i in range(1, N + 1):
    gpresum[i] = gpresum[i - 1] + gap[i - 1]
gpresum = gpresum[1:]
ans = 0
for i in range(N):
    g = gpresum[i]
    j = bisect.bisect_left(gpresum, g + H)
    l = X[j - 1][1] - X[i][0] + (H - (gpresum[j - 1] - gpresum[i]))
    ans = max(l, ans)
print(ans)
