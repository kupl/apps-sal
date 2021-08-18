import bisect
N, K = map(int, input().split())
*X, = map(int, input().split())


i = bisect.bisect_left(X, 0)
L = max(0, bisect.bisect_right(X, 0) - K)
R = min(N - 1, bisect.bisect_left(X, 0) + K - 1)

ans = float('inf')

for i in range(L, R - K + 2):
    t = 0
    l = X[i]
    r = X[i + K - 1]
    if r <= 0:
        t = abs(l)
    elif 0 <= l:
        t = r
    else:
        t = min(abs(l), r) * 2 + max(abs(l), r)
    ans = min(ans, t)
print(ans)
