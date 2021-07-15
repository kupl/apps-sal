3.5
n=int(input())
a=input().split()
b=input().split()
a.remove('0')
b.remove('0')
k=a.index(b[0])
a=a[k:]+a[:k]
if a==b:
    print('YES')
else:
    print('NO')
