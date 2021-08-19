(n, m) = map(int, input().split(' '))


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = sorted(list(set(table)))
    return table


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


s = set(divisor(n)).intersection(set(divisor(m)))
ans = 1
for ss in s:
    if len(prime_factorize(ss)) == 1:
        ans += 1
print(ans)
