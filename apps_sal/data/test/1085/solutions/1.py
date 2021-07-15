from math import sqrt, ceil


def divisors(n):
    out = []
    nn = ceil(sqrt(n))
    for i in range(1, nn):
        if n % i == 0:
            out.append(i)
            out.append(n//i)

    if nn ** 2 == n:
        out.append(nn)

    out.sort()
    return out


n = int(input())
a = len(divisors(n-1)[1:])

d = divisors(n)
for dd in d[1:]:
    nn = n
    while nn % dd == 0:
        nn = nn // dd
    if nn % dd == 1:
        a += 1

print(a)

