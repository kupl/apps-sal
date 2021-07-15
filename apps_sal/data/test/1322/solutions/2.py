def f(n, mod=10**9+7):
    ans = 1
    for i in range(1, n + 1): ans = ans * i % mod
    return ans
    
def g(n, mod=10**9+7):
    num1 = f(n * 2)
    den1 = f(n) ** 2 % mod
    return num1 * pow(den1, mod - 2, mod) % mod
    
n = int(input()) + 1
print(g(n) - 1)
