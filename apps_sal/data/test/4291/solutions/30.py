n,q=map(int,input().split())
s=input()
a=[0,0]
for l in range(1,n):
    if s[l-1]=='A' and s[l]=='C':
        a.append(a[l]+1)
    else :
        a.append(a[l])
for k in range(q):
    x,y=map(int,input().split())
    print(a[y]-a[x])
