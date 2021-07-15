n, m = map(int,input().split())
l1 = set()
l2 = set()
for i in range(m):
    a,b = map(int,input().split())
    if a==1:
        l1.add(b)
    elif b==n:
        l2.add(a)
print('POSSIBLE' if len(l1&l2) >=1 else 'IMPOSSIBLE')
