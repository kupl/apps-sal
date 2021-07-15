a=list(map(int, input().split()))
b=list(map(int, input().split()))
n=int(input())
a=sum(a)
b=sum(b)
n-=a//5
a=a%5
if a>0:
    n-=1
n-=b//10
if b%10>0:
    n-=1
if n<0:
    print('NO')
else:
    print('YES')

