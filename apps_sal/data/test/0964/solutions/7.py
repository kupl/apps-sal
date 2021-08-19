(a, b, c, d, e, f) = list(map(int, input().split()))
m = sorted([(max(a, b), min(a, b), 'A'), (max(c, d), min(c, d), 'B'), (max(e, f), min(e, f), 'C')])
ma = m[-1][0]
ma2 = ma - m[-1][1]
ans = [['A'] * ma for i in range(ma)]
if a * b + c * d + e * f != ma * ma:
    print(-1)
elif m[0][0] * m[0][1] + m[1][0] * m[1][1] != ma2 * ma:
    print(-1)
elif m[0][0] != m[1][0]:
    if m[0][0] != m[1][1] and m[0][1] != m[1][1]:
        print(-1)
    else:
        for i in range(m[-1][1]):
            for j in range(ma):
                ans[i][j] = m[-1][2]
        for i in range(m[-1][1], ma):
            for j in range(m[0][0] + m[0][1] - ma2):
                ans[i][j] = m[0][2]
        for i in range(m[-1][1], ma):
            for j in range(m[0][0] + m[0][1] - ma2, ma):
                ans[i][j] = m[1][2]
        print(ma)
        for x in ans:
            print(''.join(x))
else:
    for i in range(m[-1][1]):
        for j in range(ma):
            ans[i][j] = m[-1][2]
    if m[0][0] == ma:
        for i in range(m[-1][1], m[-1][1] + m[0][1]):
            for j in range(ma):
                ans[i][j] = m[0][2]
        for i in range(m[-1][1] + m[0][1], ma):
            for j in range(ma):
                ans[i][j] = m[1][2]
    else:
        for i in range(m[-1][1], ma):
            for j in range(m[0][1]):
                ans[i][j] = m[0][2]
        for i in range(m[-1][1], ma):
            for j in range(m[0][1], ma):
                ans[i][j] = m[1][2]
    print(ma)
    for x in ans:
        print(''.join(x))
