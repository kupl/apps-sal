n=int(input())
a=list(map(int,input().split()))
ma=0
for i in range(n):
    s=a[i]
    st=1
    while s!=1:
        if s%2==0:
            s//=2
            st*=2
        else:
            break
    if st>ma:
        ma=st
v=0
for i in range(n):
    if a[i]%ma==0:
        v+=1
print(ma,v)


