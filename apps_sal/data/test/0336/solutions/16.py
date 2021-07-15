n, a, b, c, d = [int(s) for s in input().split()]
def solve(p):
    s = []
    s.append(p[0][0] + p[0][1] + p[1][0] + p[1][1])
    s.append(p[0][1] + p[0][2] + p[1][1] + p[1][2])
    s.append(p[1][0] + p[1][1] + p[2][0] + p[2][1])
    s.append(p[1][1] + p[1][2] + p[2][1] + p[2][2])
    return max(0, n - (max(s) - min(s)))
p = [
    [0, a, 0],
    [b, 0, c],
    [0, d, 0],
]
res = 0
for m in range(1, n + 1):
    p[1][1] = m
    res += solve(p)
print(res)

