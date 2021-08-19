k = int(input())


def valid(l):
    s = 0
    for (i, n) in enumerate(l):
        s += n
        if s > 10:
            return i + 1
    if s == 10:
        return -1
    else:
        return 0


def digits(n):
    l = []
    while n > 0:
        r = n % 10
        l.append(r)
        n = n // 10
    return list(reversed(l))


i = 19
n = 0
while True:
    d = digits(i)
    r = valid(d)
    if r < 0:
        n += 1
        i += 1
    else:
        if r > 0:
            r = len(d) - r
        i = (i // 10 ** r + 1) * 10 ** r
    if n == k:
        print(i - 1)
        break
