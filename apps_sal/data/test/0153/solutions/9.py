n, k, M = map(int, input().split())
t = sorted(list(map(int, input().split())))
pt = t[:]
for i in range(1, k):
    pt[i] += pt[i - 1]
ans, r = 0, k - 1
for i in range(0, n + 1):
    if pt[-1] * i > M:
        break
    m = M - pt[-1] * i
    while r != -1 and pt[r] * (n - i) > m:
        r -= 1
    m -= (0 if r == -1 else pt[r] * (n - i))
    ans = max(ans, i * (k + 1) + (r + 1) * (n - i) + (m // t[r + 1] if r < k - 1 else 0))
print(ans)
