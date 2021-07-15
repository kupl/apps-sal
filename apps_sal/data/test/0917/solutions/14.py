n,h,m=[int(x) for x in input().split()]
counter=0
a=[h]*n
for i in range(m):
    l,r,x=[int(x) for x in input().split()]
    for i in range(l-1,r):
        a[i]=min(a[i],x,h)
for item in a:
    counter+=item**2
print(counter)

