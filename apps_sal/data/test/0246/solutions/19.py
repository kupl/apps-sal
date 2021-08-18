

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def binsearch(l, r, elem):
    n = r
    medium = (l + r) // 2
    s = medium - sum_digits(medium)
    s1 = medium - 1 - sum_digits(medium - 1)
    s2 = medium + 1 - sum_digits(medium + 1)
    while not(s2 >= elem and s < elem):
        if s < elem:
            l = medium
        elif s >= elem:
            r = medium
        k = medium
        medium = (l + r) // 2
        if k == medium:
            break
        s = medium - sum_digits(medium)
        s2 = medium + 1 - sum_digits(medium + 1)

    s1 = medium - 1 - sum_digits(medium - 1)
    if s >= elem and s1 < elem:
        return medium
    elif s2 >= elem and s < elem:
        return medium + 1
    else:
        return n + 1


n, s = list(map(int, input().split()))
if n == s:
    print(0)
else:

    y = binsearch(0, n, s)
    print(n - y + 1)
