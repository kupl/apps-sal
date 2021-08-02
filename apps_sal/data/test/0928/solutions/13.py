N, K = map(int, input().split())
a = list(map(int, input().split()))

L = 0
R = 0
rangeSum = a[0]
ans = 0
for i in range(N):
    L = i
    while rangeSum < K:
        R += 1
        if R >= len(a): break
        rangeSum += a[R]
    ans += max(N - R, 0)
    rangeSum -= a[L]
print(ans)
