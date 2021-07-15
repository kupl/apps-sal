n, m, k = map(int, input().split())
lines = [[0, 0] for i in range(n)]
columns = [[0, 0] for i in range(m)]
for i in range(k):
    task, num, color = map(int, input().split())
    if task == 1:
        lines[num-1] = [color, i+1]
    else:
        columns[num-1] = [color, i+1]
for i in range(n):
    for j in range(m):
        if lines[i][1] > columns[j][1]:
            print(lines[i][0], end = ' ')
        else:
            print(columns[j][0], end = ' ')
        
    print('')

