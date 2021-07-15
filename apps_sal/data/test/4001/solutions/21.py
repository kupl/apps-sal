n=int(input())
a=[int(i) for i in input().split()]
k=max(a)
b=[]
c=set()
for i in range(n):
    if k%a[i]==0 and a[i] not in c:
        c.add(a[i])
    else:
        b.append(a[i])
print(k,max(b))
