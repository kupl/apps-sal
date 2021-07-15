n=int(input())
a,b=[[int(x)for x in input().split()]for y in range(2)]
def ok(t):
    l,r=0,1<<30
    for x in range(n):
        l=max((a[x]-b[x]*t),l)
        r=min((a[x]+b[x]*t),r)
    return l<=r
lo,hi=0,1<<30
for i in range(65):
    m=(lo+hi)/2
    if ok(m):hi=m
    else:lo=m
print('%.10f'%hi)




# Made By Mostafa_Khaled

