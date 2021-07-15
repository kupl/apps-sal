a,b,c=input().split()
a,b,c=[int(a),int(b),int(c)]
s=0
d=[0]*(1000001)
for i in range(1,1000001):
    j=i
    while j<=1000000:
        d[j]+=1
        j+=i
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            p=(i*j*k)
            s+=d[p]
print(s)
