n, k = [int(x) for x in input().split()]
m = 998244353

facs = [1]
for i in range(1, 5*10**5 + 3):
    facs.append((facs[-1]*i) % m)

tot = 0
finvkm1 = pow(facs[k-1], m-2, m)
for i in range(1, n+1):
    # if the first number is i, then the remainder is an increasing sequence from
    # [2*i, 3*i, ..., n] or equivalently an inc seq from [1, ..., n//i - 1] of
    # length k-1. That is, it's binom(n//i - 1, k-1).
    if 0 <= k-1 <= n//i - 1:
        tot += facs[n//i - 1] * finvkm1 * pow(facs[n//i - k], m-2, m)
        tot %= m
print(tot)

