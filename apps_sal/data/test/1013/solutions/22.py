n, m = [int(x) for x in input().split()]
arr = []
for i in range(n):
    line = [int(x) for x in input().split()]
    arr.append(line)
for i in range(n):
    if arr[i][0] == 1 or arr[i][m - 1] == 1:
        print('2')
        quit()
for j in range(m):
    if arr[0][j] == 1 or arr[n - 1][j] == 1:
        print('2')
        quit()
print('4')
