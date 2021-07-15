n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
l=sorted(l)
ma=1
d={l[0]}
for i in range(1,n) :
    if l[i]/m not in d :
        d.add(l[i])
        ma+=1
print(ma)
              

