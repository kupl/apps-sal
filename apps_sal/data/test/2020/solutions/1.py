n = int(input())
useX = [False] * 101
useY = [False] * 101
cntX = 0
cntY = 0
for i in range(n):
    (x, y) = input().split(' ')
    x = int(x)
    y = int(y)
    cntX += 0 if useX[x] else 1
    cntY += 0 if useY[y] else 1
    useX[x] = True
    useY[y] = True
print(cntX if cntX < cntY else cntY)
