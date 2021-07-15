n,a,x,b,y=list(map(int,input().split()))
fl=0
while True:
    a+=1
    if a==n+1:
        a=1
    b-=1
    if b==0:
        b=n
    if a==b:
        fl=1
        break
    elif a==x or b==y:
        break
if fl:
    print('YES')
else:
    print('NO')
        

