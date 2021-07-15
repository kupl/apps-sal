N,M = list(map(int,input().split()))
L = []
for _ in range(N):
    l = list(map(int,input().split()))
    L.append(l)
cand = []
for bit in range(8):
    plus_minus = [1,1,1]
    for  b in range(3):
        if bit & (1 << b):
            plus_minus[b] = -1
    L = sorted(L, key = lambda x:x[0]*plus_minus[0]+x[1]*plus_minus[1]+x[2]*plus_minus[2])
    tmp = 0
    for i in range(M):
        for j in range(3):
            tmp += L[i][j] * plus_minus[j]
    cand.append(tmp)

print((max(abs(min(cand)),max(cand))))



