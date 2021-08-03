n, m = list(map(int, input().split()))

a = []
p = 0
v = 0

for i in range(n):
    x = input()
    a.append(x)

p = len(a)
od = 0

for i in range(m):
    x = input()
    if x in a:
        od += 1
    v += 1
if od % 2 == 0:
    v -= od
    p -= od
    if p > v:
        print('YES')
    else:
        print('NO')
else:
    if p + 1 > v:
        print('YES')
    else:
        print('NO')
