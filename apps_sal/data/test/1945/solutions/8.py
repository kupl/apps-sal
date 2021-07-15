n=int(input())
queries=[]
names=[]
f=[]
l=[]
for i in range(n):
    queries.append(input().split(' '))
for i in range(n):
    for j in range(2):
        if queries[i][j] in names:
            if j==0:
                names.remove(queries[i][j])
                l[l.index(queries[i][j])]=queries[i][j-1]
        else:
            names.append(queries[i][j])
            if j==0:
                f.append(queries[i][j])
            else:
                if queries[i][j] not in l:
                    l.append(queries[i][j])
print(len(f))
for k in range(len(f)):
    print(f[k],l[k])

