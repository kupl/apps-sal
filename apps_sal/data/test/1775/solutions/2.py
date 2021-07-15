n,m,k=map(int,input().split())
q=0
rez=[0]*int(m)
st=0
end=0
p=[[] for i in range(int(m))]
for i in range(int(n)):
        a=list(map(int,input().split()))
        c=0
        for ii in range(m):
            while p[ii] and p[ii][-1][0]<a[ii]:
                p[ii].pop()
            p[ii].append([a[ii],i])
            c+=p[ii][0][0]
        if c<=k:
            end=i+1
            if q<end-st:
                q=end-st
                for iii in range(m):
                    rez[iii]=p[iii][0][0]
        else:
            while 1==1:
                c=0
                for j in range(m):
                    if p[j] and p[j][0][1]==st:
                        p[j].pop(0)
                    if p[j]:c+=p[j][0][0]
                st+=1
                if c<=k:
                    break
            end+=1
for i in rez:
    print(i,end= " ")
