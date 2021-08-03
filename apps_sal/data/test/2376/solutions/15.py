N, W = map(int, input().split())
w1, v1 = map(int, input().split())
d = [[-v1], [], [], []]
for i in range(N - 1):
    w, v = map(int, input().split())
    x = w - w1
    d[x].append(-v)
d[0].sort()
n0 = len(d[0])
d[1].sort()
n1 = len(d[1])
d[2].sort()
n2 = len(d[2])
d[3].sort()
n3 = len(d[3])
s0 = [0]
s1 = [0]
s2 = [0]
s3 = [0]
for i in range(n0):
    x = s0[-1] + d[0][i]
    s0.append(x)
for i in range(n1):
    x = s1[-1] + d[1][i]
    s1.append(x)
for i in range(n2):
    x = s2[-1] + d[2][i]
    s2.append(x)
for i in range(n3):
    x = s3[-1] + d[3][i]
    s3.append(x)
d = [[[[0 for i in range(n3 + 1)] for j in range(n2 + 1)] for k in range(n1 + 1)] for l in range(n0 + 1)]
for i in range(n0 + 1):
    for j in range(n1 + 1):
        for k in range(n2 + 1):
            for l in range(n3 + 1):
                s = s0[i] + s1[j] + s2[k] + s3[l]
                s = -s
                x = w1 * (i + j + k + l) + j + 2 * k + 3 * l
                if x <= W:
                    d[i][j][k][l] = s
ans = 0
for i in range(n0 + 1):
    for j in range(n1 + 1):
        for k in range(n2 + 1):
            for l in range(n3 + 1):
                x = d[i][j][k][l]
                ans = max(ans, x)
print(ans)
