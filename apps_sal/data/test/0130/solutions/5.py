from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
maps = []
challengers = []

for i in range(n):
    maps.append(stdin.readline().strip())

mins = [float('inf'), float('inf')]
maxs = [float('-inf'), float('-inf')]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'B':
            if i < mins[0]:
                mins[0] = i
            
            if j < mins[1]:
                mins[1] = j
            
            if i > maxs[0]:
                maxs[0] = i
            
            if j > maxs[1]:
                maxs[1] = j

if mins != [float('inf'), float('inf')] and max(abs(maxs[1] - mins[1]), abs(maxs[0] - mins[0])) >= min(n, m):
    stdout.write('-1')
elif mins == [float('inf'), float('inf')]:
    stdout.write('1')
else:
    ans = 0
    
    for i in range(mins[0], maxs[0] + 1):
        for j in range(mins[1], maxs[1] + 1):
            if maps[i][j] != 'B':
                ans += 1
    
    if abs(maxs[1] - mins[1]) > abs(maxs[0] - mins[0]):
        ans += (abs(maxs[1] - mins[1]) - abs(maxs[0] - mins[0])) * abs(maxs[1] - mins[1] + 1)
    elif abs(maxs[1] - mins[1]) < abs(maxs[0] - mins[0]):
        ans += (abs(maxs[0] - mins[0]) - abs(maxs[1] - mins[1])) * abs(maxs[0] - mins[0] + 1)
    
    stdout.write(str(ans))
