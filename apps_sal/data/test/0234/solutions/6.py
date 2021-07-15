arr = []

def valid(i, j):
    bombs = 0
    if arr[i][j] == '*':
        return True
    if i != len(arr) - 1:
        if arr[i + 1][j] == '*':
            bombs += 1
    if i != 0:
        if arr[i - 1][j] == '*':
            bombs += 1
    if j != len(arr[0]) - 1:
        if arr[i][j + 1] == '*':
            bombs += 1
    if j != 0:
        if arr[i][j - 1] == '*':
            bombs += 1
    if i != 0 and j != 0:
        if arr[i-1][j - 1] == '*':
            bombs += 1
    if i != 0 and j != len(arr[0]) - 1:
        if arr[i-1][j + 1] == '*':
            bombs += 1
    if i != len(arr) - 1 and j != 0:
        if arr[i+1][j - 1] == '*':
            bombs += 1
    if i != len(arr) - 1 and j != len(arr[0]) - 1:
        if arr[i+1][j + 1] == '*':
            bombs += 1
    if bombs == 0 and (arr[i][j] == '.'):
        return True
    if arr[i][j] == '.':
        return False
    if int(arr[i][j]) == bombs:
        return True
    return False


n, m = list(map(int, input().split()))


for i in range(n):
    line = input()
    arr2 = []
    for j in range(m):
        arr2.append(line[j:j+1])
    arr.append(arr2)

ans = "YES"

for i in range(n):
    for j in range(m):
        if not valid(i, j):
            ans = "NO"

print(ans)



