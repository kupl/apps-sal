n = int(input())
aa = sorted(list(map(int, input().split(' '))))
bb = sorted(list(map(int, input().split(' '))))

res = 0

ai = n - 1
bi = n - 1

while ai >= 0 or bi >= 0:
    an = -1 if ai < 0 else aa[ai]
    bn = -1 if bi < 0 else bb[bi]

    if an >= bn:
        res += an
        ai -= 1
    else:
        bi -= 1

    an = -1 if ai < 0 else aa[ai]
    bn = -1 if bi < 0 else bb[bi]

    if an <= bn:
        res -= bn
        bi -= 1
    else:
        ai -= 1

print(res)
