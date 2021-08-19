N = int(input())
mod = 10 ** 9 + 7
ans = 10 ** N % mod - 9 ** N % mod * 2 + 8 ** N % mod
ans %= mod
print(ans)
