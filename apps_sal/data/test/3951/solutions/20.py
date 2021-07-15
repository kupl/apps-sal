from math import gcd
n=int(input())
l=list(map(int,input().split()))
d={}
for x in l :
    d[x]=d.get(x,0)+1
d={x:d[x]for x in sorted(d,key=lambda w:-w)}
out=[]
for x in d :
    while d[x] :
        for y in out :
            d[gcd(y,x)]-=2
        out+=[x]
        d[x]-=1
print(*out)
    
    

