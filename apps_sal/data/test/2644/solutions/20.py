
icase=0
if icase==0:
    n=int(input())
    p=list(map(int,input().split()))

for i in range(n):
    p[i]-=1

po=[0]*n
for i in range(n):
    po[p[i]]=i
    
s=[i for i in range(n-1)]
pa=[i for i in range(n)]

s=set(s)
ans=[]
#print("po:",po)
#print(p)

yn=""
for i in range(n):
#    print("i:",i,"po[i]:",po[i])
    if po[i]>i:
        for ii in range(po[i],i,-1):
#            print(p[ii],p[ii-1])
            po[p[ii]],po[p[ii-1]]=ii-1,ii
            p[ii],p[ii-1]=p[ii-1],p[ii]
#            print("ii:",ii,"p",p,"po:",po)
            if ii-1 in s:
                s.remove(ii-1)
                ans.append(ii)
            else:
                yn="no"
                break
            if len(s)==0:
                break
    elif po[i]<i:
        for ii in range(po[i],i,1):
            po[p[ii]],po[p[ii+1]]=ii+1,ii
            p[ii],p[ii+1]=p[ii+1],p[ii]
#            print("ii:",ii,"p",p,"po:",po)
#    print("i:",i,p)
            if ii-1 in s:
                s.remove(ii-1)
                ans.append(ii)
            else:
                yn="no"
                break
            if len(s)==0:
                break
    if yn=="no" or len(s)==0:
        break
    
if p==pa and len(s)==0:
    for ansi in ans:
        print(ansi)
else:
    print((-1))
    

