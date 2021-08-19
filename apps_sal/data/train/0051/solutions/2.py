def f1(d1, d2, n, k):
    a1 = 2 * d1 + d2 + k
    a2 = -d1 + d2 + k
    a3 = -d1 - 2 * d2 + k
    if a1 < 0 or a2 < 0 or a3 < 0 or a1 % 3 or a2 % 3 or a2 % 3:
        return False
    else:
        a1 //= 3
        a2 //= 3
        a3 //= 3
        (a1, a2, a3) = tuple(sorted([a1, a2, a3])[::-1])
        if a2 - a3 + 2 * (a1 - a2) > n - k:
            return False
        else:
            return True


def f2(d1, d2, n, k):
    a1 = -2 * d1 + d2 + k
    a2 = d1 + d2 + k
    a3 = d1 - 2 * d2 + k
    if a1 < 0 or a2 < 0 or a3 < 0 or a1 % 3 or a2 % 3 or a2 % 3:
        return False
    else:
        a1 //= 3
        a2 //= 3
        a3 //= 3
        (a1, a2, a3) = tuple(sorted([a1, a2, a3])[::-1])
        if a2 - a3 + 2 * (a1 - a2) > n - k:
            return False
        else:
            return True


def f3(d1, d2, n, k):
    a1 = 2 * d1 - d2 + k
    a2 = -d1 - d2 + k
    a3 = -d1 + 2 * d2 + k
    if a1 < 0 or a2 < 0 or a3 < 0 or a1 % 3 or a2 % 3 or a2 % 3:
        return False
    else:
        a1 //= 3
        a2 //= 3
        a3 //= 3
        (a1, a2, a3) = tuple(sorted([a1, a2, a3])[::-1])
        if a2 - a3 + 2 * (a1 - a2) > n - k:
            return False
        else:
            return True


def f4(d1, d2, n, k):
    a1 = -2 * d1 - d2 + k
    a2 = d1 - d2 + k
    a3 = d1 + 2 * d2 + k
    if a1 < 0 or a2 < 0 or a3 < 0 or a1 % 3 or a2 % 3 or a2 % 3:
        return False
    else:
        a1 //= 3
        a2 //= 3
        a3 //= 3
        (a1, a2, a3) = tuple(sorted([a1, a2, a3])[::-1])
        if a2 - a3 + 2 * (a1 - a2) > n - k:
            return False
        else:
            return True


a = []
z = int(input())
for i in range(z):
    (n, k, d1, d2) = map(int, input().split())
    v1 = f1(d1, d2, n, k)
    v2 = f2(d1, d2, n, k)
    v3 = f3(d1, d2, n, k)
    v4 = f4(d1, d2, n, k)
    if (v1 or v2 or v3 or v4) and n % 3 == 0:
        a.append('yes')
    else:
        a.append('no')
print(*a, sep='\n')
