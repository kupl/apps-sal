n=int(input())
a=sum(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
if b[-1]+b[-2] >= a:
    print('YES')
else:
    print('NO')
