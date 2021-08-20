def solve(n, u, v):
    res = (n * (n + 1) * (2 * n + 1) // 6 + n * (n + 1) // 2) // 2
    for (l, r) in zip(u, v):
        if l > r:
            (l, r) = (r, l)
        res -= l * (n - r + 1)
    return res


n = int(input())
u = [0] * n
v = [0] * n
for i in range(n - 1):
    (u[i], v[i]) = map(int, input().split())
print(solve(n, u, v))
