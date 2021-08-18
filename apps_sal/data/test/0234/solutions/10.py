n, m = list(map(int, input().split()))
arr = [[0 for _ in range(m + 2)]] + [[] for _ in range(n)] + [[0 for _ in range(m + 2)]]

for i in range(1, n + 1):
    s = input()
    arr[i].append(0)
    for j in s:
        if j == '*':
            arr[i].append(-1)
        elif j == '.':
            arr[i].append(0)
        else:
            arr[i].append(int(j))
    arr[i].append(0)

flag = True
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (arr[i][j] != -1) and (((arr[i - 1][j - 1] == -1) + (arr[i - 1][j] == -1) + (arr[i - 1][j + 1] == -1) +
           (arr[i][j - 1] == -1) + (arr[i][j + 1] == -1) +
           (arr[i + 1][j - 1] == -1) + (arr[i + 1][j] == -1) + (arr[i + 1][j + 1] == -1)) != arr[i][j]):
            flag = False
            break
    if not flag:
        break
if flag:
    print('YES')
else:
    print('NO')
