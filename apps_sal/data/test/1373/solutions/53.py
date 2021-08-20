(n, k) = map(int, input().split())
mod = 10 ** 9 + 7
sum1 = 0
for i in range(k, n + 2):
    sum1 += (-i * (i - 1) // 2 + i * (2 * n - i + 1) // 2 + 1) % mod
print(sum1 % mod)
