n,m=list(map(int,input().split()))
l=[int(input(),2) for i in range(n)]
c=int('1'*m,2)
b=True
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        if i!=j:
            s=s|l[j]
    if s==c:
        b=False
        print('YES')
        break
if b:
    print('NO')

