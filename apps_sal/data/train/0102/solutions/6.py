N = int(input())


def check(n, cifra):
    f = cifra
    count = 0
    while cifra <= n:
        cifra = cifra * 10 + f
        count += 1
    return count


for i in range(N):
    a = int(input())
    print(check(a, 1) + check(a, 2) + check(a, 3) + check(a, 4) + check(a, 5) + check(a, 6) + check(a, 7) + check(a, 8) + check(a, 9))
