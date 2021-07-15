n=int(input())
m=list(map(int,input().split()))
p=list(map(int,input().split()))
a=max(p)
p.remove(a)
b=max(p)
s=sum(m)
if s>a+b:
    print('NO')
else:
    print('YES')
