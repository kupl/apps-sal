n=int(input())
a=[int(x) for x in input().split()]
s=sum(a)
if max(a)<=s-max(a) and s%2==0:
    print('YES')
else:
    print('NO')

