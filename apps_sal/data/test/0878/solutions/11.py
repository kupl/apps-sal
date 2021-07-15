n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(1,len(a)):
    if a[i]+a[i-1]==5:
        c=0
        break
    elif a[i]+a[i-1]==4:
        c+=4
    elif a[i]+a[i-1]==3:
        c+=3
    if a[i-2]==3 and a[i-1]==1 and a[i]==2:
        c-=1
if c==0:
    print('Infinite')
else:
    print('Finite')
    print(c)
