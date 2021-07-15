n=int(input())
l=[int(i) for i in input().split()]
ans=0 
f=0 
#l.insert0(10000000000000,0)
for i in range(n-1,0,-1):
    if l[i]<l[i-1]:
        print(i)
        f=1 
        break 
if not f:
    print(f)
