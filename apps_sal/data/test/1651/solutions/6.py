s, p = map(int, input().split())
d = s**2 - 4 * p


def sd(a):
    s = int(a**.5)
    while (1 + s)**2 <= a: s += 1
    return s


x = sd(d)
if s >= x >= 0 and d == x**2 and (x + s) % 2 == 0: print("Yes")
else: print("No")
