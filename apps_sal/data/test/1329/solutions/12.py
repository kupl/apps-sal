import collections

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


count = 0
div = {}
for i in range(2, n + 1):
    c = collections.Counter(prime_factorize(i))
    for key, value in list(c.items()):
        if key in div:
            div[key] += value
        else:
            div[key] = 1


def num(m):
    return len(list([x for x in list(div.values()) if x + 1 >= m]))


print((num(75) + num(25) * (num(3) - 1) + num(15)
      * (num( 5)-1) + num(5)*(num(5)-1)*(num(3)-2)//2))
