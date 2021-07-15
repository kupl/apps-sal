n,s=map(int,input().split())
a=list(map(int,input().split()))
a=sorted(a)
if sum(a[0:n-1])<=s:
    print('YES')
else:
    print('NO')
