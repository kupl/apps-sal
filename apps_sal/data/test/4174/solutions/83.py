a,b=map(int,input().split())
l=list(map(int,input().split()))
c=[0]
count=1
for i in range(a):
    c.append(c[i]+l[i])
    if(c[i+1]<=b):
        count+=1
print(count)
