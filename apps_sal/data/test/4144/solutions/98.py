n = int(input())
mod = 10**9+7
ans = pow(10, n, mod)-2*pow(9, n, mod)+pow(8, n, mod)
ans %= mod
print(ans)
