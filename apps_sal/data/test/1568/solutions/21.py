a,b,c,d,e=map(int,input().split())
k=list(map(int,input().split()))
k.sort()
i=0
x=0
while i<len(k):
    if k[i]<=e:
        if d>c:
            x=x+b+(d-c)*(e-k[i])
        else:
            x=x+b
    else:
        break
    i=i+1
print (x)
