p, k = list(map(int, input().split()))


def convert(num, base):
    res = []
    if num == 0:
        res = [0]
    else:
        res = []
        while num != 0:
            num, rem = divmod(num, -base)
            if rem < 0:
                num, rem = num + 1, rem + base
            res.append(rem)
    return res


res = convert(p, k)
print(len(res))
print(' '.join([str(x) for x in res]))
