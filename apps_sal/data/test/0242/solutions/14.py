import math
m = int(input())


def f(k):
    res = 0
    power = 5
    l = math.ceil(math.log(k, 5))
    for i in range(1, l + 2):
        res += k // power
        power *= 5
    return res


def pok(k):
    res = 0

    while k % 5 == 0:
        res += 1
        k = k // 5
    return res


s = 4 * m + 5 - ((4 * m) % 5)
t = f(s)
out = 0
while t < m:
    s += 5

    t += pok(s)
if t != m:
    print(0)
else:
    print(5)
    print(" ".join([str(z) for z in [s, s + 1, s + 2, s + 3, s + 4]]))
