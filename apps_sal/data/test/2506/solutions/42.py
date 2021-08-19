from bisect import bisect_left
(N, M) = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
l = 0
r = 2 * 10 ** 5 + 5
while l + 1 < r:
    mid = (l + r) // 2
    m = 0
    for a in A:
        idx = bisect_left(A, mid - a)
        m += N - idx
    if m >= M:
        l = mid
    else:
        r = mid
s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + A[i]
ans = 0
m = 0
for a in A:
    idx = bisect_left(A, l - a)
    m += N - idx
    ans += s[N] - s[idx]
    ans += a * (N - idx)
ans -= (m - M) * l
print(ans)
