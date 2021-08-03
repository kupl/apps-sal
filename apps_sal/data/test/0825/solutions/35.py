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


l = prime_factorize(N)
L = set(l)
z = 0
for j in L:
    i = 1
    while i * (i + 1) // 2 <= l.count(j):
        i += 1
    z += i - 1
print(z)
