mirror = [8, -1, -1, 3, 6, 9, 4, 7, 0, 5]


def dg(n):
    if n:
        res = []
        while n:
            res.append(n % 10)
            n //= 10
    else:
        res = [0]
    return res


n = int(input())
dg1 = dg(n)
dg2 = [mirror[d] for d in reversed(dg1)]
if dg1 == dg2:
    print('Yes')
else:
    print('No')
