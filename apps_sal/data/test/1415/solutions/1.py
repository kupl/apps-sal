(x, y, x0, y0) = map(int, input().split())
moves = input()
seen = [[False] * y for i in range(x)]
(currX, currY) = (x0 - 1, y0 - 1)
total = 0
for i in range(len(moves)):
    if not seen[currX][currY]:
        print('1', end=' ')
        total += 1
    else:
        print('0', end=' ')
    seen[currX][currY] = True
    if moves[i] == 'L':
        currY = max(currY - 1, 0)
    elif moves[i] == 'R':
        currY = min(currY + 1, y - 1)
    elif moves[i] == 'U':
        currX = max(currX - 1, 0)
    else:
        currX = min(currX + 1, x - 1)
print(x * y - total)
