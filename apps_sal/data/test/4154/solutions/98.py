N,M = map(int,input().split())
lsL = []
lsR = []
for i in range(M):
    L,R = map(int,input().split())
    lsL.append(L)
    lsR.append(R)
print(max(0,min(lsR)-max(lsL)+1))
