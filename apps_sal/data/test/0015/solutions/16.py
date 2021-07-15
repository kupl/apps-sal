a,b,c=list(map(int,input().split()))

if c==0:
    if a==b:
        print('YES')
    else:
        print('NO')
else:
    k=(b-a)/c
    if int(k)-k==0.0 and k>=0:
        print("YES")
    else:
        print('NO')

