m,n=[int(x) for x in input().split()]
s=set()
for i in range(m):
    L=[int(x) for x in input().split()]
    for i in range(1,len(L)):
        s.add(L[i])
if len(s)==n:
    print('YES')
else:
    print('NO')

