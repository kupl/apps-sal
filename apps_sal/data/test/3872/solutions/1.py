import collections

a = input()
b = input()
ca = collections.Counter(a)
cb = collections.Counter(b)


def eq(a, b, ah, at, bh, bt):
    if a[ah:at] == b[bh:bt]:
        return True
    len_a = at - ah
    if (len_a % 2) == 1:
        return False
    half = len_a // 2
    am = ah + half
    bm = bh + half
    return (eq(a, b, ah, am, bm, bt) and eq(a, b, am, at, bh, bm)) or (eq(a, b, ah, am, bh, bm) and eq(a, b, am, at, bm, bt))


if ca != cb:
    print('NO')
elif eq(a, b, 0, len(a), 0, len(b)):
    print('YES')
else:
    print('NO')
