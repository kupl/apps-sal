import sys
3


def solve(a, b, c):
    (ix, iy, iz) = (3, 2, 1)
    if b < a:
        (a, b) = (b, a)
        (ix, iy) = (iy, ix)
    if c < a:
        (a, c) = (c, a)
        (iz, iy) = (iy, iz)
    if c < b:
        (b, c) = (c, b)
        (iz, ix) = (ix, iz)
    x2 = a + (c - b)
    if x2 % 2 != 0:
        print('Impossible')
        return
    x = x2 // 2
    z = a - x
    y = c - x
    s = list(sorted([x, y, z]))
    if not all([n >= 0 for n in s]):
        print('Impossible')
        return
    if s.count(0) > 1:
        print('Impossible')
        return
    sol = [(ix, x), (iy, y), (iz, z)]
    sol.sort()
    print(sol[0][1], sol[1][1], sol[2][1])


(a, b, c) = [int(x) for x in sys.stdin.readline().strip().split()]
solve(a, b, c)
