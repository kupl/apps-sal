import numpy as np
(H, W, K) = list(map(int, input().split()))
C = np.zeros((H, W))
for i in range(H):
    c = input()
    for j in range(len(c)):
        if c[j] == '#':
            C[i][j] = 1
CH = []
CW = []
for i in range(2 ** H):
    cl = []
    for j in range(H):
        if bin(i)[-j - 1] == '1':
            cl.append(j)
        elif bin(i)[-j - 1] == 'b':
            break
    CH.append(cl)
for i in range(2 ** W):
    cl = []
    for j in range(W):
        if bin(i)[-j - 1] == '1':
            cl.append(j)
        elif bin(i)[-j - 1] == 'b':
            break
    CW.append(cl)
ans = 0
for i in range(len(CH)):
    for j in range(len(CW)):
        count = 0
        for k in range(len(CH[i])):
            for l in range(len(CW[j])):
                count += C[CH[i][k]][CW[j][l]]
        if count == K:
            ans += 1
print(ans)
