n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for _ in range(n)]


def test(a, n ,m):
    for i in range(n):
        _or, _and = a[i][0], a[i][0]
        for j in range(m):
            _or |= a[i][j]
            _and &= a[i][j]
        if _or != _and:
            return i
    return -1

t = test(a, n, m)
if t == -1:
    _xor = 0
    for i in range(n):
        _xor ^= a[i][0]
    if _xor > 0:
        print('TAK')
        print(' '.join('1' for _ in range(n)))
        return
else:
    _xor = 0
    for i in range(n):
        if i == t:
            continue
        _xor ^= a[i][0]
    for j in range(m):
        if _xor ^ a[t][j] > 0:
            print('TAK')
            print(' '.join(['1' if k != t else str(j + 1) for k in range(n)]))
            return
print('NIE')

