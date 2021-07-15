[n, m, p] = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]


coord_change = [[0,1],[0,-1],[1,0],[-1,0]]

grid = []

visited = [[False]*1010 for x in range(1010)]

queue = [[] for x in range(10)]
controlled = [0]*10

for i in range(n):
    grid.append(input())
    for j in range(m):
        if grid[i][j] == '.':
            continue
        elif grid[i][j] == '#':
            visited[i][j] = True
        else:
            player = int(grid[i][j])-1
            visited[i][j] = True
            queue[player].append([i,j])
            controlled[player] += 1



curr_p = 0
while any(queue):
    moves = 0
    # print(curr_p, queue,s)
    while moves < s[curr_p] and queue[curr_p]:
        new_queue = []
        curr_queue = queue[curr_p]
        for coord in curr_queue:
            for change in coord_change:
                new_coord = [coord[0]+change[0],coord[1]+change[1]]
                if new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= n or new_coord[1] >= m:
                    continue
                if visited[new_coord[0]][new_coord[1]]:
                    continue

                visited[new_coord[0]][new_coord[1]] = True
                controlled[curr_p] += 1
                new_queue.append(new_coord)
        moves += 1
        queue[curr_p] = new_queue
    curr_p += 1
    curr_p %= p

# print(grid[0])
# print(controlled)
for i in range(p):
    print(controlled[i],end=' ')
