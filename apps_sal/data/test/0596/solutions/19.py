dm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap(y):
    return y % 4 == 0 and y != 1900


def dn(y, m, d):
    return d + sum(dm[i] + (i == 2 and leap(y)) for i in range(m))


d = sorted(list(map(int, input().split(':'))) for i in range(2))
if d[0][0] == d[1][0]:
    print(dn(*d[1]) - dn(*d[0]))
else:
    print(365 + leap(d[0][0]) - dn(*d[0]) + sum(365 + leap(i) for i in range(d[0][0] + 1, d[1][0])) + dn(*d[1]))
