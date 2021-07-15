import heapq

X,Y,Z,K = [int(x) for x in input().split()]
XYZ=[0]*3
for i in range(3):
    XYZ[i]=[int(x)for x in input().split()]
    XYZ[i].sort(reverse=True)


tmp = (-1*(XYZ[0][0]+XYZ[1][0]+XYZ[2][0]),0,0,0)
q = [tmp]
inq = {tmp[1:]}
heapq.heapify(q)

for ik in range(K):
    max = heapq.heappop(q)
    print((-max[0]))
    i,j,k = max[1],max[2],max[3]
    #print(-max[0],i,j,k)
    if(not ((i+1,j,k) in inq) and i+1 < X):
        heapq.heappush(q,(-1*(XYZ[0][i+1]+XYZ[1][j]+XYZ[2][k]),i+1,j,k))
        inq.add((i+1,j,k))
    if(not ((i,j+1,k) in inq) and j+1 < Y):
        heapq.heappush(q,(-1*(XYZ[0][i]+XYZ[1][j+1]+XYZ[2][k]),i,j+1,k))
        inq.add((i,j+1,k))
    if(not ((i,j,k+1) in inq) and k+1 < Z):
        heapq.heappush(q,(-1*(XYZ[0][i]+XYZ[1][j]+XYZ[2][k+1]),i,j,k+1))
        inq.add((i,j,k+1))
print()

