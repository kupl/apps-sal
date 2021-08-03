n = int(input())


def check(p):
    c = 0
    while p > 0:
        c += p % 10
        p //= 10
    return c


if n % check(n) == 0:
    print("Yes")
else:
    print("No")
