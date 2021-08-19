(n, m) = map(int, input().split())
b1 = []
b2 = []
for i in range(m):
    (a, b) = map(int, input().split())
    if a == 1:
        b1.append(b)
    if b == n:
        b2.append(a)
if len(b1) + len(b2) == len(list(set(b1 + b2))):
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
