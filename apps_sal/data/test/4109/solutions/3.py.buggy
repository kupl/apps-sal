import numpy as np
N, M, X = map(int, input().split())

C = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    #C=[[0 for i in range(M)] for j in range(2**N)]
    C[i] = list(map(int, input().split()))
    # print(array)
    # np.insert(C[i],0,array)
D = np.array(C)
E = [0] * 2**N

for i in range(2**N):
    c = format(i, '012b')
    for j in range(N):
        d = int(c[12 - N + j])
        E[i] += D[j] * int(d)
# print(E)

# for i in range(2**M):
if min(E[-1][1:M + 1]) < X:
    print(-1)
    return

Max = E[-1][0] + 1
Min = Max
for i in range(2**N):
    if min(E[i][1:M + 1]) >= X:
        if Min > E[i][0]:
            Min = E[i][0]
        continue
    else:
        E[i][0] = Max
# print(E)
print(Min)
return
