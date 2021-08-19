from collections import Counter


def getList(l, m):
    r = []
    cnt = Counter(l)
    for i in l:
        r.extend([cnt[i]])
    return r


m = int(input())
res = []
for i in range(m):
    (a, b) = [i for i in input().split('/')]
    a = a.split('+')
    aux1 = a[0].replace('(', '')
    aux2 = a[len(a) - 1].replace(')', '')
    a = [aux1, aux2]
    a = list(map(lambda x: int(x), a))
    b = float(b)
    res.extend([sum(a) / b])
output = getList(res, m)
for i in range(len(output)):
    if i == len(output) - 1:
        print(output[i])
    else:
        print(str(output[i]) + ' ', end='')
