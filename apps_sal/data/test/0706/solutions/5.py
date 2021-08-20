(A, B, n, x) = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
if A != 1:
    A_n = pow(A, n, mod)
    ans = A_n * x % mod + (1 - A_n) * B * pow(1 - A, mod - 2, mod) % mod
else:
    ans = x + B * n
ans %= mod
print(ans)
