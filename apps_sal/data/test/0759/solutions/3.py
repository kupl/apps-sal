hh, mm = [int(v) for v in input().split()]
H, D, C, N = [int(v) for v in input().split()]


def dvru(a, b):
    return (a + b - 1) // b


if hh >= 20:
    print(dvru(H, N) * (C * 0.8))
else:
    c1 = dvru(H, N) * C
    t = (20 - hh - 1) * 60 + (60 - mm)
    c2 = dvru(H + t * D, N) * (C * 0.8)
    print(min(c1, c2))
