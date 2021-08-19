(n, m) = map(int, input().split())
p = 10 ** 9 + 7


def pow(a, n):
    w = 1
    mn = a
    while n > 0:
        if n % 2 == 1:
            w = w * mn % p
        mn = mn * mn % p
        n //= 2
    return w


print(pow(pow(2, m) - 1, n))
