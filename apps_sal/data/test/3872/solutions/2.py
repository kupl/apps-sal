import collections

a = input()
b = input()
ca = collections.Counter(a)
cb = collections.Counter(b)


def eq(a, b):
    if a == b:
        return True
    len_a = len(a)
    if (len_a % 2) == 1:
        return False
    half = len_a // 2
    a1 = a[:half]
    a2 = a[half:]
    b1 = b[:half]
    b2 = b[half:]
    return (eq(a1, b2) and eq(a2, b1)) or (eq(a1, b1) and eq(a2, b2))

if ca != cb:
    print('NO')
elif eq(a, b):
    print('YES')
else:
    print('NO')
