a, b = map(int, input().split())


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


A = set(prime_factorize(a))
B = set(prime_factorize(b))

cnt = 0
for i in A:
    if i in B:
        cnt += 1
print(cnt + 1)
