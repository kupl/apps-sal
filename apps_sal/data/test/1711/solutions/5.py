#!/usr/bin/env python3

MOD = 998244353
n,m = list(map(int,input().split()))

def go(a, b, c):
    ans = 1
    while b > 0:
        if b%2 == 1:
            ans *= a
            ans %= c
        b //= 2
        a *= a
        a %= c
    return ans

if n == 2:
    print(0)
else:
    start = (n-2)*go(2, n-3, MOD)
    start %= MOD
    bunja = 1
    bunmo = 1
    for i in range(n, m+1):
        bunja *= i
        bunmo *= (i-n+1)
        bunja %= MOD
        bunmo %= MOD

    #ans = start * bunja // bunmo
    start *= bunja
    temp = go(bunmo, MOD-2, MOD)
    ans = start * temp
    ans %= MOD
    print(ans)

