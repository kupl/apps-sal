n = int(input())
b = 0
currentPos = 0
for i in range(n):
    k, dir = input().split()
    k = int(k)
    if currentPos == 0 and dir != 'South':
        b = 1
    elif currentPos == 20000 and dir != 'North':
        b = 1
    elif dir == 'North' and currentPos - k < 0:
        b = 1
    elif dir == 'South' and currentPos + k > 20000:
        b = 1
    else:
        if dir == 'North':
            currentPos -= k
        elif dir == 'South':
            currentPos += k
if currentPos != 0:
    b = 1
if b == 0:
    print('YES')
else:
    print('NO')
