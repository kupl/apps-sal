(n, k) = map(int, input().split())
M = [n] * (n + 1)
m = [0] * (n + 1)
for i in range(1, n + 1):
    M[i] = M[i - 1] + n - i
    m[i] = m[i - 1] + i
mod = 10 ** 9 + 7
ans = 0
for i in range(k - 1, n + 1):
    tmp = M[i] - m[i] + 1
    ans = (ans + tmp) % mod
ans = ans % mod
print(ans)
