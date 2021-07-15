n,c=list(map(int,input().split()))
v=[int(i) for i in input().split()]
d=v[0]
m=1
for i in range(1,n):
    if(v[i]-d>c):
        m=1
    else:
        m=m+1
    d=v[i]
print(m)
    

