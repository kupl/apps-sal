n, m = list(map(int, input().split()))
arr = [[0 for i in range(m)] for j in range(n)]
fl = 0
for i in range(n):
    mass = input()
    for j in range(m):
        if mass[j] == '.':
            arr[i][j] = 0
        elif mass[j] == '*':
            arr[i][j] = -1
        else:
            arr[i][j] = int(mass[j])

for i in range(n):
    for j in range(m):
        if(arr[i][j] != -1):
            c = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if(i + x >= 0 and i + x < n and j + y >= 0 and j + y < m):
                        if(arr[i + x][j + y] == -1):
                            c += 1
            if(c != arr[i][j]):
                fl = 1
if(fl == 0):
    print('YES')
else:
    print("NO")
