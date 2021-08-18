mod = 10 ** 9 + 7
x, y = [int(i) for i in input().split()]
if (2 * x - y) % 3 != 0 or (2 * y - x) % 3 != 0:
    print(0)
    return
a = (2 * x - y) // 3
b = (2 * y - x) // 3
if a < 0 or b < 0:
    print(0)
    return


def mygcd(a_b, b, mod):
    b = min(a_b, b)
    cnt = 1
    for i in range(b):
        cnt = cnt * (a_b - i) * pow(i + 1, mod - 2, mod) % mod
    return cnt


print(mygcd(a + b, b, mod))
