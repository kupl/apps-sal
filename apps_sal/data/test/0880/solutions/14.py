def factorial_mod(n, mod):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) % mod
    return ans

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    mod = 998244353
    len_metaseq = factorial_mod(n, mod)
    ans = (
        ((n - 1) + (n - 2)) *
        len_metaseq *
        499122177 # modinv(2, mod)
    ) % mod
    error = 0
    for curr in range(4, n + 1):
        error = ((error + 1) * curr) % mod
    return (ans - error) % mod

n = int(input())
print(solve(n))
