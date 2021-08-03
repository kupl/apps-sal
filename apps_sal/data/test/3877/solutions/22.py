def get(nn, x):
    res = 0
    i = -1
    while x:
        res += ((x + 1) // 2) * nn[i]
        x //= 2
        i -= 1
    return res


def toBin(n):
    res = []
    while n:
        res.append(n % 2)
        n //= 2
    if res:
        return res
    else:
        return [0]


def raw(n):
    if n < 2:
        return [n]
    else:
        temp = raw(n // 2)
        return temp + [n % 2] + temp


n, l, r = list(map(int, input().split()))
nn = toBin(n)
print(get(nn, r) - get(nn, l - 1))
