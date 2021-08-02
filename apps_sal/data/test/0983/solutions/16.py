import sys
# =int(input())
# =list(map(int, input().split()))
n, p, q, r = list(map(int, input().split()))
a = list(map(int, input().split()))
minil = [0] * n
minir = [0] * n
maxil = [0] * n
maxir = [0] * n
minil[0] = maxil[0] = a[0]
minir[n - 1] = maxir[n - 1] = a[n - 1]
for i in range(1, n):
    minil[i] = min(minil[i - 1], a[i])
    maxil[i] = max(maxil[i - 1], a[i])
for i in range(n - 2, -1, -1):
    minir[i] = min(minir[i + 1], a[i])
    maxir[i] = max(maxir[i + 1], a[i])
ans = 0
tans = -10**19
for i in range(n):
    ans = q * a[i]
    ans += max(p * minil[i], p * maxil[i])
    ans += max(r * minir[i], r * maxir[i])
    tans = max(tans, ans)
print(tans)
