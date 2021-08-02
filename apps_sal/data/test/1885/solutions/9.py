def cnk(n, k):
    return f[n] // f[n - k] // f[k]


n = int(input())

f = [0 for i in range(n + 1)]
f[0] = 1
for i in range(1, n + 1):
    f[i] = f[i - 1] * i
ans = 0
for i in range(5, 8):
    if (i <= n):
        ans += cnk(n, i)
print(ans)
