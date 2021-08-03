n, m = [int(x) for x in input().split()]

arr = []

x1, x2, y1, y2 = 101, -1, 101, -1

for i in range(n):
    arr.append(input().rstrip())
c1 = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "B":
            x1 = min(x1, j)
            x2 = max(x2, j)
            y1 = min(y1, i)
            y2 = max(y2, i)
            c1 = 1

#print(x1, x2, y1, y2)

count = 0

for j in range(x1, x2 + 1):
    for i in range(y1, y2 + 1):
        if arr[i][j] == "W":
            count += 1

sizeX = x2 - x1 + 1
sizeY = y2 - y1 + 1
if not c1:
    print(1)
elif sizeX > sizeY:
    if sizeX > n:
        print(-1)
    else:
        print(count + sizeX * (sizeX - sizeY))
elif sizeY > sizeX:
    if sizeY > m:
        print(-1)
    else:
        print(count + sizeY * (sizeY - sizeX))
else:
    print(count)
