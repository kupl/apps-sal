import numpy as np
H, W = map(int, input().split())
mat = []
for _ in range(H):
    a = list(input())
    ca = [0 if i == '.' else 1 for i in a]
    mat.append(ca)
amat = np.array(mat)

mask1 = []
for i in range(H):
    if np.sum(amat[i]) != 0:
        mask1.append(i)
amat1 = amat[mask1]

mask2 = []
for i in range(W):
    if np.sum(amat1[:,i]) != 0:
        mask2.append(i)
amat2 = amat1[:,mask2]

ans = []
for i in range(amat2.shape[0]):
    temp = ''
    for s in amat2[i]:
        if s == 1:
            temp += '#'
        else:
            temp += '.'
    ans.append(temp)
print(*ans, sep='\n')

