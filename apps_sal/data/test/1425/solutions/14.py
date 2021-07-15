n=int(input())
v=[int(i) for i in input().split()]
v.sort()
if(v[n-1]>=v[n-2]+v[n-3]):
    print('NO')
else:
    print('YES')
    t=v[n-2]
    v[n-2]=v[n-1]
    v[n-1]=t
    for i in v:
        print(i, end=' ')

