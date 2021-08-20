A = list(map(int, input().split()))
b = list(map(int, input().split()))


def convert(x, y):
    return (y + x, y - x)


AX = []
AY = []
BX = []
BY = []
for i in range(4):
    (x, y) = convert(b[2 * i], b[2 * i + 1])
    if x not in BX:
        BX.append(x)
    if y not in BY:
        BY.append(y)
    if A[2 * i] not in AX:
        AX.append(A[2 * i])
    if A[2 * i + 1] not in AY:
        AY.append(A[2 * i + 1])
AX.sort()
AY.sort()
BX.sort()
BY.sort()
for i in range(-111, 111):
    for j in range(-111, 111):
        (I, J) = convert(i, j)
        if AX[0] <= i <= AX[1] and BX[0] <= I <= BX[1] and (AY[0] <= j <= AY[1]) and (BY[0] <= J <= BY[1]):
            print('YES')
            quit()
print('NO')
