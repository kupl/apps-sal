n,m=map(int,input().split())
if m==0:
    print("YES")
    return
a=set(map(int,input().split()))
l=0
for i in a:
    if (i+1 in a)and(i+2 in a):
        l+=1
if (1 in a) or (n in a)or(l>0):
    print('NO')
else:
    print('YES')
