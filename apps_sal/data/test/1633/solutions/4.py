n, m, k = map(int, input().split())
answer = [[False for i in range(m)] for i in range(n)]
flag = False
for i in range(k):
    x, y = map(int, input().split())
    if x <= n - 1 and y <= m - 1:
        if answer[x][y]:
            if answer[x - 1][y] and answer[x][y - 1]:
                print(i + 1)
                flag = True
                break
    if x - 2 >= 0 and y - 2 >= 0:
        if answer[x - 2][y - 2]:
            if answer[x - 1][y - 2] and answer[x - 2][y - 1]:
                print(i + 1)
                flag = True
                break
    if x - 2 >= 0 and y <= m - 1:
        if answer[x - 2][y]:
            if answer[x - 1][y] and answer[x - 2][y - 1]:
                print(i + 1)
                flag = True
                break
    if x <= n - 1 and y >= 2:
        if answer[x][y - 2]:
            if answer[x][y - 1] and answer[x - 1][y - 2]:
                print(i + 1)
                flag = True
                break
    answer[x - 1][y - 1] = True

for j in range(i + 1, k):
    x, y = map(int, input().split())
if flag == False:
    print(0)
