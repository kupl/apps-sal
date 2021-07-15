n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    b=bin(i)[:1:-1]
    for j in range(len(b)):
        if int(b[j]):
            d[j]=d.get(j,[])
            d[j].append(i)
for i in range(31,-1,-1):
    if len(d.get(i,[]))==1:
        v=d[i].pop()
        print(v,end=' ')
        k=0
        for j in l:
            if j==v and k<1:k+=1
            else:print(j,end=' ')
        quit()
print(' '.join(map(str,l)))
