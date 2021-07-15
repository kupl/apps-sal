n,m = map(int,input().split())
ls = [[] for _ in range(n+1)]
di = []
for i in range(m):
    a,b = map(int,input().split())
    ls[a].append([b,i+1])
for j in range(n+1):
    if ls[j] != []:
        ls[j].sort(key=lambda x :x[0])
        for k in range(len(ls[j])):
            di.append([ls[j][k][1],str(10**12+j*10**6+k+1)[1:]])
di.sort(key=lambda x :x[0])
for l in range(m):
    print(di[l][1])
