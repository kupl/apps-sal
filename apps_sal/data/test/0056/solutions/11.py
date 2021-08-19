(n, t) = list(map(int, input().split()))
m = [[0] * 11 for i in range(11)]
eps = 1e-06
for l in range(t):
    m[0][0] += 1.0
    for i in range(n):
        for j in range(i + 1):
            if m[i][j] - eps > 1.0:
                should_end = False
                delta = m[i][j] - 1.0
                m[i][j] = 1.0
                m[i + 1][j] += delta / 2.0
                m[i + 1][j + 1] += delta / 2.0
answ = 0
for i in range(n):
    for j in range(n):
        if abs(m[i][j] - 1.0) <= eps:
            answ += 1
print(answ)
