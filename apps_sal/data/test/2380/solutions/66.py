N,M = map(int,input().split())
lsA = list(map(int,input().split()))
lsM = []
for i in range(M):
    B,C = map(int,input().split())
    lsM.append([B,C])
lsA.sort()
lsM.sort(key=lambda x:-x[1])
k = 0
for i in range(M):
    B = lsM[i][0]
    C = lsM[i][1]
    ii = 1
    for j in range(B):
        if lsA[k] < C and ii <= B:
            lsA[k] = C
            if k == N-1:
                break
            k += 1
            ii += 1        
    if k == N-1 or lsA[k] >= C:
        break
print(sum(lsA))
