input()


def f():
    return (' ' + input()).replace(' 0', '')


(a, b) = (f(), f())
print('YES' if a in b + b else 'NO')
