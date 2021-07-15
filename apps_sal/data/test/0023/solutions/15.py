import bisect

def get_int(l, xa, j):
    return int(''.join(l + [xa[j]] + sorted(xa[:j] + xa[j+1:])))

def f(a, b):
    if len(a) < len(b):
        return int(''.join(reversed(sorted(a))))
    xa = list(sorted(a))
    xb = list(b)
    ib = int(b)
    m = int(''.join(xa))

    l = []
    for i in range(len(xb)):
        mj, r = 0, 0
        for j in range(len(xa)):
            if get_int(l, xa, j) <= ib:
                r = get_int(l, xa, j)
                mj = j
        l.append(xa[mj])
        xa = xa[:mj] + xa[mj+1:]

    return int(''.join(l))

def test_f():
    assert f('123', '222') == 213
    assert f('129', '1000') == 921
    assert f('125', '222') == 215
    assert f('4940', '5000') == 4940
    assert f('321', '500') == 321


a = input()
b = input()
print(f(a, b))

