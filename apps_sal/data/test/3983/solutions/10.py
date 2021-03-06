from collections import Counter as C


class F:

    def __init__(self, n):
        self.n = n
        self.p = list(R(n))
        self.r = [1] * n

    def f(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.f(self.p[x])
            return self.p[x]

    def T(self, x, y):
        p = self.f(x)
        q = self.f(y)
        if p == q:
            return None
        if p > q:
            (p, q) = (q, p)
        self.r[p] += self.r[q]
        self.p[q] = p


(I, R, A, B) = (input, range, 'First', 'Second')
for _ in R(int(I())):
    (n, m) = map(int, I().split())
    U = F(n)
    for i in R(m):
        (a, b) = map(int, I().split())
        U.T(a - 1, b - 1)
    if n % 2:
        print(A if (n * (n - 1) // 2 - m) % 2 else B)
    else:
        for i in R(n):
            U.f(i)
        c = C(U.p)
        (x, y) = (c[U.f(0)], c[U.f(n - 1)])
        print(A if x % 2 != y % 2 else A if (n * (n - 1) // 2 - x * y - m) % 2 else B)
