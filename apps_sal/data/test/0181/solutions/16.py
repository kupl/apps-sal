import sys


def chet(a, b):
    ans = (b - a) // 2
    if b % 2 == 0 or a % 2 == 0:
        ans += 1
    return ans


def nechet(a, b):
    ans = (b - a) // 2
    if b % 2 == 1 or a % 2 == 1:
        ans += 1
    return ans


def ans(a, b, c, d):
    return chet(a, c) * chet(b, d) + nechet(a, c) * nechet(b, d)


n = int(input())
ras = n // 360
k = n - 360 * ras
ost = (k + 45) % 90
d = (k + 45) // 90
ans = d if (ost > 0 or d % 4 == 0) else d - 1
print(ans % 4)







