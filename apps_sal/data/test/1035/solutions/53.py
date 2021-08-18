
a, b = list(map(int, input().split()))


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


a_prime = set(prime_factorize(a))
b_prime = set(prime_factorize(b))
ans = 0
for ap in a_prime:
    for bp in b_prime:
        if ap == bp:
            ans += 1
            break
print((ans + 1))
