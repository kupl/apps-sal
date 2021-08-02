def mul(a, b, mod):
    c = [[0] * len(b[0]) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
                if c[i][j] > mod:
                    c[i][j] %= mod
    return c


def power(val, p, mod):
    ans = [[1 if j == i else 0 for j in range(len(val))] for i in range(len(val))]
    while p:
        if p & 1:
            ans = mul(ans, val, mod)
        val = mul(val, val, mod)
        p >>= 1
    return ans;


n, f1, f2, f3, x = list(map(int, input().split()))
n -= 1
mod = 1000000007
b1 = [[0], [0], [1]]
b2 = [[0], [1], [0]]
b3 = [[1], [0], [0]]
bc = [[0], [0], [0], [4], [1]]
m1 = m2 = m3 = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
mc = [
    [1, 1, 1, 2, -6],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]
a = pow(f1, mul(power(m1, n - 2, mod - 1), b1, mod - 1)[0][0], mod)
b = pow(f2, mul(power(m2, n - 2, mod - 1), b2, mod - 1)[0][0], mod)
c = pow(f3, mul(power(m3, n - 2, mod - 1), b3, mod - 1)[0][0], mod)
print(pow(x, mul(power(mc, n - 2, mod - 1), bc, mod - 1)[0][0], mod) * a * b * c % mod)
