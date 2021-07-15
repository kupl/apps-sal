n=int(input())
ip=list(map(int,input().split()))
v={'a','e','i','o','u','y'}
b=0
for i in range(n):
    s=str(input())
    count=0
    for j in s:
        if j in v:
            count+=1
    if count!=ip[i]:
        b=1
        break
if b==0:
    print('YES')
else:
    print('NO')

