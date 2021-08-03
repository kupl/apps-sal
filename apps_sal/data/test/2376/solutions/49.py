n, w = list(map(int, input().split()))
w_sub, v_sub = list(map(int, input().split()))
w0 = w_sub
inf = 1000000001
x = [[inf, v_sub], [inf], [inf], [inf]]
for i in range(n - 1):
    w_sub, v_sub = list(map(int, input().split()))
    z = w_sub - w0
    x[z].append(v_sub)
for i in range(4):
    x[i].sort(key=lambda x: -x)
    x[i][0] = 0
    l_sub = len(x[i])
    for j in range(1, l_sub):
        x[i][j] += x[i][j - 1]

ma = 0
l3 = len(x[3])
l2 = len(x[2])
l1 = len(x[1])
l0 = len(x[0])
for i in range(l3):
    for j in range(l2):
        d = w - i * (w0 + 3) - j * (w0 + 2)
        if d >= 0:
            for k in range(l1):
                d = w - i * (w0 + 3) - j * (w0 + 2) - k * (w0 + 1)
                if d >= 0:
                    ma = max(ma, x[3][i] + x[2][j] + x[1][k] + x[0][min(d // w0, l0 - 1)])
                else:
                    break
        else:
            break

print(ma)
