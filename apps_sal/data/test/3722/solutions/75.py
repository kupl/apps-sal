def printn(x):
    return print(x, end='')


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


def inm():
    return map(int, input().split())


def ins():
    return input().strip()


DBG = True
BIG = 10 ** 18
R = 10 ** 9 + 7


def ddprint(x):
    if DBG:
        print(x)


n = inn()
aa = ins()
ab = ins()
ba = ins()
bb = ins()
if ab == 'A' and aa == 'A' or (ab == 'B' and bb == 'B'):
    print(1)
elif ab == 'A' and aa == 'B' and (ba == 'A') or (ab == 'B' and bb == 'A' and (ba == 'B')):
    d = [0] * (n + 1)
    d[0] = 1
    for i in range(2, n + 1):
        for j in range(i - 1):
            d[i] = (d[i] + d[j]) % R
    print(d[n])
else:
    d = [0] * (n + 1)
    d[0] = 1
    x = 1
    for i in range(2, n - 1):
        for j in range(i - 1):
            d[i] = (d[i] + d[j] * (i - j - 1)) % R
        x = (x + d[i]) % R
    print(x)
