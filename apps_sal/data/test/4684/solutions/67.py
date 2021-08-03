n = ''

for s in input().split():
    n += s

if int(n) % 4 == 0:
    print('YES')
else:
    print('NO')
