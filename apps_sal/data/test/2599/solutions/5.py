def f(sm, nine):
    if sm < 0:
        return -1
    if nine * 9 > sm:
        return -1
    sm -= nine * 9
    ret = nine * '9'
    if sm >= 8:
        sm -= 8
        ret = '8' + ret
    ret = str(sm % 9) + (sm // 9) * '9' + ret
    return int(ret)


def g(sm, lstmax):
    mn = min(sm, lstmax)
    sm -= lstmax
    ret = str(sm % 9) + (sm // 9) * '9' + str(mn)
    return int(ret)


def digit_sum(n):
    s = str(n)
    return sum(int(i) for i in s)


def nc(i):
    return i * (i + 1) // 2


def valid(n, k):
    n %= 10
    if n + k >= 10:
        return False
    return True


def naive(n, k):
    c = 0
    sm = 0
    for i in range(k + 1):
        sm += digit_sum(c + i)
    for _ in range(10**6):
        if sm == n:
            return c
        sm -= digit_sum(c)
        c += 1
        sm += digit_sum(c + k)
    else:
        return -1


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    mp = k * (k + 1) // 2
    res = 10 ** 100

    if n - mp > 0 and (n - mp) % (k + 1) == 0:
        fx = (n - mp) // (k + 1)
        res = min(res, g(fx, 9 - k))

    for i in range(k + 1):
        for j in range(1, 30):
            mp = nc(k - i) - nc(i)
            if (n + 9 * j * (k - i) - mp) > 0 and (n + 9 * j * (k - i) - mp) % (k + 1) == 0:
                fx = (n + 9 * j * (k - i) - mp) // (k + 1)
                if f(fx, j) - i < 0:
                    continue
                res = min(res, f(fx, j) - i)

    for i in range(400):
        tmp = 0
        for j in range(k + 1):
            tmp += digit_sum(i + j)
        if tmp == n:
            res = min(res, i)
            break

    if res == 10 ** 100:
        res = -1
    print(res)
