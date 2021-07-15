import sys
k1,k2,k3=list(map(int,input().split()))
L=[k1,k2,k3]
x=L.count(1)
if x!=0:
    print("YES")
    return
x=L.count(2)
if x>=2:
    print('YES')
    return
x=L.count(3)
if x==3:
    print("YES")
    return
if L.count(4)==2 and L.count(2)==1:
    print("YES")
    return
print("NO")


