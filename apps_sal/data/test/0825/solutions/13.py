import copy
n = int(input())


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


L = prime_factorize(n)
M = L.copy()
M = list(set(M))

cnt = 0
for x in M:
    m = L.count(x)
    for i in range(L.count(x)):
        if m - i - 1 >= 0:
            m -= i + 1
            cnt += 1

print(cnt)
