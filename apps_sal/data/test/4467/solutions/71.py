n = int(input())
aka = [[0 for i in range(2 * n)] for j in range(2 * n)]
for i in range(n):
    (a, b) = list(map(int, input().split()))
    aka[a][b] = 1
ao = [tuple(map(int, input().split())) for i in range(n)]
ao.sort()
ans = 0
for (x, y) in ao:
    flag = False
    for j in reversed(list(range(y))):
        if flag:
            break
        for i in reversed(list(range(x))):
            if aka[i][j] == 1:
                ans += 1
                aka[i][j] = 0
                flag = True
                break
print(ans)
