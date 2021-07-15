x,k=list(map(int,input().split()))
s=set()
for i in range(k):
    a=list(map(int,input().split()))
    if a[0]==1:
        s.add(a[1])
        s.add(a[2])
    else:
        s.add(a[1])
smax=set()
smin=set()
for i in range(1,x):
    if not i in s and not i+1 in s and not i in smin:
        smin.add(i+1)
    if not i in s:
        smax.add(i)
    if not i in s and i+1 in s:
        smin.add(i)
print(len(smin),len(smax))

