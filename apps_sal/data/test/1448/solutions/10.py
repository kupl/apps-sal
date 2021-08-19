class Vec:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __mod__(self, other):
        return self.x * other.y - self.y * other.x


(n, d) = map(int, input().split())
m = int(input())
c = [[int(e) for e in input().split()] for i in range(m)]
(pa, pb, pc, pd) = (Vec(d, 0), Vec(n, n - d), Vec(n - d, n), Vec(0, d))
(ab, bc, cd, da) = (pb - pa, pc - pb, pd - pc, pa - pd)
for (x, y) in c:
    p = Vec(x, y)
    (ap, bp, cp, dp) = (p - pa, p - pb, p - pc, p - pd)
    if ab % ap >= 0 and bc % bp >= 0 and (cd % cp >= 0) and (da % dp >= 0):
        print('YES')
    else:
        print('NO')
