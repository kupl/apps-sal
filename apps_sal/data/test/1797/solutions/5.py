n=int(input())
p=[0]*(n+1)
p[1:n+1]=list(map(int,input().split()))
c=[]
used=[False]*(n+1)
for i in range(1,n+1):
    if used[i]:
        continue
    s=list()
    s.append(i)
    used[i]=True
    j=p[i]
    while not used[j]:
        s.append(j)
        used[j]=True
        j=p[j]
    c.append(len(s))
if len(c)==1:
    print(n*n)
else:
    c.sort()
    c.reverse()
    #print(c)
    m=c[0]+c[1]
    print(m*m+sum([d*d for d in c[2:]]))



