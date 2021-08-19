ps = [tuple(map(int, str.split(input()))) for _ in range(int(input()))]
lx = rx = ty = by = None


def foo(v, cv, f):
    return cv if v is None else f(v, cv)


for (x, y) in ps:
    lx = foo(lx, x, min)
    rx = foo(rx, x, max)
    by = foo(by, y, min)
    ty = foo(ty, y, max)
print(max(abs(lx - rx), abs(by - ty)) ** 2)
