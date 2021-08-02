n = int(input())
tx = 0
ty = 20000
res = True
for i in range(n):
    t, d = map(str, input().split())
    if d == 'South':
        ty -= int(t)
        if ty < 0:
            res = False
    elif d == 'North':
        ty += int(t)
        if ty > 20000:
            res = False
    elif d == 'West':
        tx -= int(t)
        if ty == 0 or ty == 20000:
            res = False
    elif d == 'East':
        tx += int(t)
        if ty == 0 or ty == 20000:
            res = False
if res and ty == 20000:
    print('YES')
else:
    print('NO')
