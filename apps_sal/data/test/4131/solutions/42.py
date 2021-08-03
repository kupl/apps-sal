N, M = list(map(int, input().split()))
P = [0] * M
for i in range(M):
    P[i] = list(map(int, input().split())) + [i + 1]

P = sorted(P, key=lambda x: x[1])
P = sorted(P, key=lambda x: x[0])

a = P[0][0]
c = 0
for i in range(M):
    # print(P[i])
    if P[i][0] == a:
        c += 1
        P[i].append(c)
    else:
        c = 1
        a = P[i][0]
        P[i].append(c)
    # print(P[i])

P = sorted(P, key=lambda x: x[2])
for i in range(M):
    s = str(P[i][0]).zfill(6)
    ss = str(P[i][3]).zfill(6)
    print((s + ss))
