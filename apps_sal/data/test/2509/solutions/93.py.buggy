n, k = [int(x) for x in input().split()]

if k == 0:
    print(n ** 2)
    return

ans = 0
for b in range(k + 1, n + 1):
    q, mod = divmod(n, b)
    ans += q * (b - k)
    if mod >= k:
        ans += mod - k + 1
print(ans)
