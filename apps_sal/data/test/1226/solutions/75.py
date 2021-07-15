from math import factorial
n, a, b = [int(i) for i in input().split()]
mod = 10 ** 9 + 7

def nCr(n, r):
    nonlocal mod
    ans = 1
    for i in range(r):
        ans = (ans * (n-i)) % mod
    return (ans * pow(factorial(r), mod-2, mod)) % mod

print((pow(2, n, mod) - nCr(n, a) - nCr(n, b) - 1) % mod) 
