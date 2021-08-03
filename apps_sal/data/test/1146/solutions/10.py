n, m = input().split()
n = int(n)
m = int(m)

l = set()
for i in range(n):
    ll = list(map(int, input().split()))
    for j in ll[1:]:
        l.add(j)
if len(l) == m:
    print('YES')
else:
    print('NO')
