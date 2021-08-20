def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


(n, L) = mi()
C = li()
for i in range(1, n):
    C[i] = min(C[i], C[i - 1] * 2)
x = 2 ** (n - 1)
y = 0
z = 10 ** 18
for i in range(n - 1, -1, -1):
    t = L // x
    y += C[i] * t
    z = min(z, y + C[i])
    L %= x
    x //= 2
z = min(z, y)
print(z)
