inputs = [x for x in input().split()]
(n, p, t) = (int(inputs[0]), float(inputs[1]), int(inputs[2]))
saved = [[0 for _ in range(n)] for _ in range(t)]
saved[0][0] = p
for i in range(1, t):
    saved[i][0] = saved[i - 1][0] + (1 - saved[i - 1][0]) * p
for i in range(1, t):
    for j in range(1, n):
        saved[i][j] = saved[i - 1][j - 1] * p + saved[i - 1][j] * (1 - p)
print(sum(saved[-1]))
