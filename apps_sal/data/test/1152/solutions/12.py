N,M = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]

if N==1 or M==1:
    print('Yes' if A==B else 'No')
    return

D = []
for arow,brow in zip(A,B):
    D.append([abs(a-b) for a,b in zip(arow,brow)])

for i in range(N-1):
    ds = [j for j in range(M) if D[i][j]]
    if len(ds)%2:
        print('No')
        return
    for j in ds:
        D[i+1][j] = 1 - D[i+1][j]
print('No' if any(D[-1]) else 'Yes')    

