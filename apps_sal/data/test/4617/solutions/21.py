x = str(input())
y = str(input())
conditions = x[0] == y[2] and x[1] == y[1] and (x[2] == y[0])
if conditions:
    print('YES')
else:
    print('NO')
