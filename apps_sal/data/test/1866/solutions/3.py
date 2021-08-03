n = int(input())


def f(x, a):
    if x == 2:
        return [(a, a + 1)]
    else:
        s = []
        for i in range(x // 2):
            s += [(a + i, a + i + x // 2)]
        return f(x // 2, a) + f(x // 2, x // 2 + a) + s


if n == 0 or n == 1:
    print(0)
else:
    x = 1
    for i in range(1, n):

        if 2 * x > n:
            break
        x *= 2
    s1 = f(x, 1)
    s2 = f(x, n - x + 1)
    print(len(s1) + len(s2))
    for i in range(len(s1)):
        print(s1[i][0], s1[i][1])
    for i in range(len(s2)):
        print(s2[i][0], s2[i][1])
