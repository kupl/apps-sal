def f(n):
    m = int(n ** 0.5) + 1
    t = [1, 0] * (n // 2 + 1)
    t[0], t[1], t[2] = 1, 1, 0
    for i in range(3, m):
        if t[i] == 0: t[i * i:: 2 * i] = [1] * ((n - i * i) // (2 * i) + 1)
    for i in range(n - 1, -1, -1):
        if t[i]: t[i] = t[i + 1] + 1
    return t


q = f(100007)
n, m = list(map(int, input().split()))
t = [[q[j] for j in map(int, input().split())] for i in range(n)]

print(min(min(sum(t[i]) for i in range(n)), min(sum(t[i][j] for i in range(n)) for j in range(m))))
