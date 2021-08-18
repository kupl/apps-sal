import collections


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f**2 <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


count = 0
N = int(input())

if N <= 1:
    print(0)
    return
else:
    c = collections.Counter(prime_factorize(N))

    K = [sum(range(1, i)) for i in range(2, 11)]
    # = [1, 3, 6, 10, 15, 21, 28, 36, 45]

    for i in c:
        for j in range(1, len(K)):
            if c[i] < K[j]:
                count += j
                break

    print(count)
