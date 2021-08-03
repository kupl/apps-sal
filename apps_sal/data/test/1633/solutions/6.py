n, m, k = input().split(' ')
n = int(n)
m = int(m)
k = int(k)
moves = []
grid = []
count = 0
ind = 0
dead = False
for i in range(k):
    a, b = input().split(' ')
    moves.append([int(a), int(b)])
for i in range(n):
    grid.append([])
    for j in range(m):
        grid[i].append(0)
while not dead:
    try:
        move = moves[count]
    except IndexError:
        break
    else:
        move = moves[count]
    count += 1
    dr1 = False
    dr2 = False
    dr3 = False
    dr4 = False
    grid[move[0] - 1][move[1] - 1] = 1
    if move[0] >= 2 and move[1] <= m - 1:
        dr1 = True
    if move[0] >= 2 and move[1] >= 2:
        dr2 = True
    if move[0] <= n - 1 and move[1] >= 2:
        dr3 = True
    if move[0] <= n - 1 and move[1] <= m - 1:
        dr4 = True
    if dr1:
        if grid[move[0] - 2][move[1]] and grid[move[0] - 2][move[1] - 1] and grid[move[0] - 1][move[1]]:
            dead = True
    if dr2:
        if grid[move[0] - 2][move[1] - 2] and grid[move[0] - 2][move[1] - 1] and grid[move[0] - 1][move[1] - 2]:
            dead = True
    if dr3:
        if grid[move[0]][move[1] - 2] and grid[move[0]][move[1] - 1] and grid[move[0] - 1][move[1] - 2]:
            dead = True
    if dr4:
        if grid[move[0]][move[1]] and grid[move[0] - 1][move[1]] and grid[move[0]][move[1] - 1]:
            dead = True
if dead:
    print(count)
else:
    print(0)
