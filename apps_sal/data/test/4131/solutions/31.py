N, M = map(int, input().split())
P = [list(map(int, input().split())) for i in range(M)]
for i in range(M):
    P[i].append(i)
P.sort(key=lambda x: x[1])
B = [1] * N

for i in range(M):
    P[i] += "0" * (6 - len(str(P[i][0]))) + str(P[i][0]) + "0" * (6 - len(str(B[P[i][0] - 1]))) + str(B[P[i][0] - 1]),
    B[P[i][0] - 1] += 1

P.sort(key=lambda x: x[2])
for i in range(M):
    print(P[i][3])
