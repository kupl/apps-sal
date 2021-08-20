(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
for i in range(k, n + 2):
    l = i * (1 + i) // 2
    r = i * (n + 1 - i + 1 + (n + 1)) // 2
    ans = (ans + r - l + 1) % mod
print(ans)
