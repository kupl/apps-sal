b=list(map(int,input().split()))
a=[]
for i in range(1,b[0]+1):
    a.append(i)
c=a[:b[1]+1]
c.reverse()
a=c+a[b[1]+1:]
for j in a:
    print(j,end=' ')

