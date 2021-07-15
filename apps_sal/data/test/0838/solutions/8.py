n,m=list(map(int,input().split()))
rc=[]
cc=[]
cols=[[] for i in range(m)]
for i in range(n):
    a=list(map(int,input().split()))
    for i in range(len(a)):
        cols[i].append(a[i])
    rc.append([a.count(1),a.count(0)])
for i in cols:
    cc.append([i.count(1),i.count(0)])

total=0
for i in rc:
    total+=(2**i[0])-1+(2**i[1])-1
for i in cc:
    total+=(2**i[0]-1-i[0])+(2**i[1]-1-i[1])
print(total)
                

