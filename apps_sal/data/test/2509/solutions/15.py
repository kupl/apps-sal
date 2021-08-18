n, k = map(int, input().split())


ans = 0
for b in range(1, n + 1):
    ans += (n // b) * max(0, b - k) + max(n % b + 1 - k, 0)
    if k == 0:
        ans -= 1
print(ans, flush=True)
