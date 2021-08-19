(a, b, c) = map(int, input().split())


def s(x):
    xStr = str(x)
    sum = 0
    for c in xStr:
        sum += int(c)
    return sum


rightSide = []
M = 9 * 9 + 1
for k in range(1, M):
    rightSide.append(b * k ** a + c)
myList = []
sol = 0
for x in rightSide:
    if x > 0 and x < int(1000000000.0) and (x == b * s(x) ** a + c):
        sol += 1
        myList.append(x)
myList.sort()
print(sol, end='\n')
for num in myList:
    print(num, sep=' ', end=' ')
