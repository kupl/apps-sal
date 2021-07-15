N,M = map(int,input().split())
inf = 10 ** 6

d = [[inf]*N for i in range(N)]
prev = [[N]*N for i in range(N)]
vlist = [[0]*N for i in range(N)]

for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    vlist[a][b] = 1
    vlist[b][a] = 1
    d[a][b] = c
    d[b][a] = c
    prev[a][b] = a
    prev[b][a] = b

#####
#print("d",d)
#print("vlist",vlist)
#print("prev",prev)
#####

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                prev[i][j] = prev[k][j]

for i in range(N):
    for j in range(N):
        if prev[i][j] == i:
            vlist[i][j] = 0

#####
#print("d",d)
#print("vlist",vlist)
#print("prev",prev)
#####

count = 0
for i in range(N-1):
    for j in range(i,N):
        if vlist[i][j] == 1 and vlist[j][i] == 1:
            count += 1

print(count)
