import sys
N = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

res = []
result = 1
for I in range(2,N+1):
    res += prime_factorize(I)
for J in set(res):
    result *= res.count(J) + 1
print(result % (10**9+7))
