# F
from operator import mul
from functools import reduce

r1, c1, r2, c2 = [int(i) for i in input().split()]
mod = 10**9 + 7

# pre-caluculation of the factorial
num = 10**6 * 2 + 3
fact = [0] * num
fact[0] = 1
for i in range(1, num):
    fact[i] = (fact[i - 1] * i) % mod


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def f(rr, cc):
    # (0,0)~(r,c)までのコンビネーションの累積和
    #print(rr+cc+2, cc+1)
    #print(combinations_count(rr+cc+2, cc+1))
    # return combinations_count(rr+cc+2, cc+1) - 1
    return (fact[rr + cc + 2] % mod * pow(fact[rr + 1] * fact[cc + 1], mod - 2, mod)) % mod - 1


ans = f(r2, c2) - f(r2, c1 - 1) - f(r1 - 1, c2) + f(r1 - 1, c1 - 1)
print(ans % mod)
