from numpy.linalg import matrix_power
from numpy import dot, array


class mint:
    def __init__(self, n):
        self.n = n % mod

    def __add__(self, other):
        return mint(self.n + other.n)

    def __mul__(self, other):
        return mint(self.n * other.n)

    def __repr__(self):
        return str(self.n)


L, A, B, mod = map(int, input().split())

ans = array([mint(0), mint(A), mint(B)])

size = 0
for d in range(1, 19):
    x = pow(10, d, mod)
    T = array([
        [mint(x), mint(0), mint(0)],
        [mint(1), mint(1), mint(0)],
        [mint(0), mint(1), mint(1)],
    ])

    cnt = min(L - size, max(0, 10 ** d - 1 - A) // B - size + 1)
    if cnt > 0:
        ans = dot(ans, matrix_power(T, cnt))

    size += cnt
    if size >= L:
        break

print(ans[0])
