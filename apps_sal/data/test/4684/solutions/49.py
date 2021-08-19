(r, g, b) = map(int, input().split())
result = int('{}{}{}'.format(r, g, b))
if result % 4 == 0:
    print('YES')
else:
    print('NO')
