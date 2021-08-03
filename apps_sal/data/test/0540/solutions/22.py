
def is_path_exist(cage, visited, i1, j1, i2, j2):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    temp_point = []
    reached = False
    stk_adj = []
    stk_adj.append([i1, j1])
    cage[i1][j1] = 'X'
    while(len(stk_adj) and not reached):
        temp_point = stk_adj.pop()
        for i in range(0, 4):
            if ((temp_point[0] + dx[i] > -1 and temp_point[0] + dx[i] < len(cage)) and
                (temp_point[1] + dy[i] > -1 and temp_point[1] + dy[i] < len(cage[0])) and
                    visited[temp_point[0] + dx[i]][temp_point[1] + dy[i]] == False):
                if (temp_point[0] + dx[i] == i2 and temp_point[1] + dy[i] == j2):
                    reached = True
                    break
                if (cage[temp_point[0] + dx[i]][temp_point[1] + dy[i]] != 'X'):
                    visited[temp_point[0] + dx[i]][temp_point[1] + dy[i]] = True
                    stk_adj.append([temp_point[0] + dx[i], temp_point[1] + dy[i]])
    return reached


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
numbers = list(map(int, input().split()))
n = int(numbers[0])
m = int(numbers[1])
temp_line = ""
cage = []

visited = [[False] * m for _ in range(n)]
for i in range(0, n):
    cage.append([])
    temp_line = input()
    for j in range(0, m):
        cage[i].append(temp_line[j])
numbers = list(map(int, input().split()))
i1 = int(numbers[0] - 1)
j1 = int(numbers[1] - 1)
numbers = list(map(int, input().split()))
i2 = int(numbers[0] - 1)
j2 = int(numbers[1] - 1)
pos = 0
if(is_path_exist(cage, visited, i1, j1, i2, j2)):
    if(cage[i2][j2] == 'X'):
        print('YES')
        pos = 1
    if(pos == 0):
        count = 0
        for i in range(0, 4):
            if (i2 + dx[i] > -1 and i2 + dx[i] < len(cage) and j2 + dy[i] > -1 and j2 + dy[i] < len(cage[0]) and
                    (cage[i2 + dx[i]][j2 + dy[i]] == '.' or (i2 + dx[i] == i1 and j2 + dy[i] == j1)) ):
                count += 1
        if(count > 1):
            print('YES')
        else:
            print('NO')
else:
    print('NO')
