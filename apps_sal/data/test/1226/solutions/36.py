def nCk(n, k, mod):
    nu = 1
    de = 1 
    for i in range(1, k+1):
        nu *= (n-i+1)
        de *= i
        nu = nu % mod
        de = de % mod
    ans = nu * pow(de, mod-2, mod) % mod
    return ans

n, a, b = map(int, input().split())
mod = 10**9+7
ans = (pow(2, n, mod) - 1 - nCk(n, a, mod) - nCk(n, b, mod)) % mod
print(ans)
