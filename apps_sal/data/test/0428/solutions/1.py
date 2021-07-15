mod, sx, sy, dx, dy, t = list(map(int, input().split()))
class Matrix():
    def __init__(self, n):
        self.n = n
        self.a = [[0] * n for _ in range(n)]

    def __mul__(self, b):
        res = Matrix(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    res.a[i][j] += self.a[i][k] * b.a[k][j] % mod
                    res.a[i][j] %= mod
        return res

    def __pow__(self, e):
        res = Matrix(self.n)
        for i in range(self.n):
            res.a[i][i] = 1
        tmp = self
        while e:
            if e & 1:
                res = res * tmp
            e >>= 1
            tmp = tmp * tmp
        return res
M = Matrix(6)
M.a = [[2, 1, 1, 0, 1, 2],
       [1, 2, 0, 1, 1, 2],
       [1, 1, 1, 0, 1, 2],
       [1, 1, 0, 1, 1, 2],
       [0, 0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0, 1]]
sx -= 1
sy -= 1
r = M ** t
f = lambda i: (r.a[i][0] * sx + r.a[i][1] * sy + r.a[i][2] * dx + r.a[i][3] * dy + r.a[i][5]) % mod + 1
print(f(0), f(1))

