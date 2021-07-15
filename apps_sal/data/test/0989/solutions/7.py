n,k=list(map(int,input().split()))
li=list(map(int,input().split()))
d={}
l=[]
for i in li:
    try:
        d[i]+=1
    except KeyError:
        d[i]=1
        l.append(i)
l.sort()
z=1
a=0
b=len(l)-1
while k>0:
    if a==b:
        z=0
        break
    if d[l[a]]>d[l[b]]:
        s=d[l[b]]*(l[b]-l[b-1])
        if s<=k:
            k-=s
            d[l[b-1]]+=d[l[b]]
            b-=1
        else:
            b1=k//d[l[b]]
            z=2
            break
    else:
        s=d[l[a]]*(l[a+1]-l[a])
        if s<=k:
            k-=s
            d[l[a+1]]+=d[l[a]]
            a+=1
        else:
            a1=k//d[l[a]]
            z=3
            break
        
if z==0:
    print(0)
elif z==1:
    print(l[b]-l[a])
elif z==2:
    print(l[b]-l[a]-b1)
else:
    print(l[b]-l[a]-a1)


