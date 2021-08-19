q = 100010


def rop():
    a = [1] * q
    a[0] = 0
    s = [True] * q
    s[0] = s[1] = False
    for i in range(2, q):
        if s[i]:
            o = i
            while o < q:
                s[o] = False
                a[o] *= -1
                o += i
            o = i ** 2
            while o < q:
                a[o] = 0
                o += i ** 2
    return a


d = int(input())
a = rop()


def pro(x):
    return pow(x, 10 ** 9 + 5, 10 ** 9 + 7)


f = 1
for i in range(2, q):
    z = d // i * pro(d)
    f += -a[i] * z * pro(1 - z)
print(f % (10 ** 9 + 7))
