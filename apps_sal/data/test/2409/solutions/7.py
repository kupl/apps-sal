f=lambda:map(int,input().split())
t,=f()
for _ in[0]*t:
    n,k,l=f();s=[*f()];a=0;z=k-1
    for i in s:
        if i+k<=l:z=k-1
        elif z>=0and l>=i:z=min(z,l-i)-1
        elif l<i or abs(z)>l-i:a=1
        else:z-=1
    print('YNeos'[a::2])
