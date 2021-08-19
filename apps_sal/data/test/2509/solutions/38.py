(n, k) = map(int, input().split())
ans = 0
for b in range(1, n + 1):
    p = n // b
    r = n % b
    ans += p * max(0, b - k) + max(0, r - k + 1)
if k == 0:
    ans -= n
print(ans)
