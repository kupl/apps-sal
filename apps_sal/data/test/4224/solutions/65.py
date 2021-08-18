
N = int(input())
a = list(map(int, input().split()))


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


fact_list = []
for item in a:
    fact_list += prime_factorize(item)

print((fact_list.count(2)))
