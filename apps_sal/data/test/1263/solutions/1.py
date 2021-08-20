(n, k) = map(int, input().split())
(x, y) = ([0] * 100001, [0] * 100001)
x[0] = y[0] = 1
g = h = 0
for (u, v) in zip(*(map(int, input().split()), map(int, input().split()))):
    d = u - k * v
    if d > 0:
        for j in range(g, -1, -1):
            if x[j]:
                x[j + d] = max(x[j + d], x[j] + v)
        g += d
    else:
        for j in range(h, -1, -1):
            if y[j]:
                y[j - d] = max(y[j - d], y[j] + v)
        h -= d
s = max((x[i] + y[i] for i in range(min(g, h) + 1) if x[i] and y[i])) - 2
print(k * s - (not s))
