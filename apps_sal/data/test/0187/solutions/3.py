n = int(input())
a = [int(input()) for i in range(n)]
a.sort()
b = [ai for ai in a if ai==a[0]]
c = [ai for ai in a if ai!=a[0]]
if len(b)==len(c) and c[0]==c[-1]:
    print('YES')
    print(b[0], c[0])
else:
    print('NO')
