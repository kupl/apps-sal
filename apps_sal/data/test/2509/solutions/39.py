n, k = list(map(int, input().split()))

ans = 0

for b in range(k + 1, n + 1):
    s = n // b
    a = n % b
    ans += s * (b - k)
    ans += max(a - k + 1, 0)
    if k == 0:
        ans -= 1

print(ans)
