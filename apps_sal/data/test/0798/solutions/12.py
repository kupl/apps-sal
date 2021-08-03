a, b, c = list(map(int, input().split()))
l = [(a, 0), (b, 1), (c, 2)]
l.sort()
m = {}
(a, x), (b, y), (c, z) = l
if a + b >= c and (a + b - c) % 2 == 0:
    tmp = m[(x, y)] = m[(y, x)] = (a + b - c) // 2
    m[(x, z)] = m[(z, x)] = a - tmp
    m[(y, z)] = m[(z, y)] = b - tmp
    print(m[(0, 1)], m[(1, 2)], m[(0, 2)])
else:
    print('Impossible')
