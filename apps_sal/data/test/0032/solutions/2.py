n = int(input())
cur = 0
for i in range(n):
    (dist, typ) = input().split()
    dist = int(dist)
    if typ in ['West', 'East']:
        if cur in [0, 20000]:
            print('NO')
            break
        continue
    if typ == 'North':
        if cur < dist:
            print('NO')
            break
        cur -= dist
    elif typ == 'South':
        if 20000 - cur < dist:
            print('NO')
            break
        cur += dist
else:
    if cur != 0:
        print('NO')
    else:
        print('YES')
