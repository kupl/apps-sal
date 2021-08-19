def reorder(a):
    length = len(a)
    if length % 2 == 1:
        return a
    else:
        p_a = reorder(a[:length // 2])
        s_a = reorder(a[length // 2:])
        if p_a < s_a:
            return p_a + s_a
        else:
            return s_a + p_a


if reorder(input()) == reorder(input()):
    print('YES')
else:
    print('NO')
