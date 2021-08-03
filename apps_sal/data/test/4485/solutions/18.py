n, m = map(int, input().split())

l1 = []
l2 = []
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        l1.append(b)
    elif b == n:
        l2.append(a)

if len(set(l1) & set(l2)) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
