cost = [
    [3, 3, 0, 4, 4, 0, 3, 3],
    [3, 3, 0, 4, 4, 0, 3, 3],
    [2, 2, 0, 3, 3, 0, 2, 2],
    [2, 2, 0, 3, 3, 0, 2, 2],
    [1, 1, 0, 2, 2, 0, 1, 1],
    [1, 1, 0, 2, 2, 0, 1, 1]]

arr = []
ans = 0

for row in range(6):
    arr.append(input())
    for col in range(8):
        if cost[row][col] > ans and arr[row][col] == '.':
            ans = cost[row][col]

for row in range(6):
    for col in range(8):
        if cost[row][col] == ans and arr[row][col] == '.':
            arr[row] = arr[row][:col] + 'P' + arr[row][col + 1:]
            ans = -1
            break
    print(arr[row])
