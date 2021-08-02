n, m = [int(i) for i in input().split()]
stars = []
directionx = [0, -1, 0, 1]
directiony = [1, 0, -1, 0]
for i in range(n):
    stars.append(list(input()))

s = 0
f = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if stars[i][j] == "*":
            s += 1

anslist = []
ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (stars[i][j] == "*") and (stars[i][j - 1] == "*") and (stars[i - 1][j] == "*") and (stars[i][j + 1] == "*") and (stars[i + 1][j] == "*"):
            wkf = True
            count = 0
            while wkf:
                for k in range(4):
                    f[i + directionx[k] * count][j + directiony[k] * count] = True
                count += 1
                for k in range(4):
                    if i + directionx[k] * count >= n:
                        wkf = False
                        break
                    if j + directiony[k] * count >= m:
                        wkf = False
                        break
                    if i + directionx[k] * count < 0:
                        wkf = False
                        break
                    if j + directiony[k] * count < 0:
                        wkf = False
                        break
                    if stars[i + directionx[k] * count][j + directiony[k] * count] != "*":
                        wkf = False
                        break
            anslist.append([i + 1, j + 1, count - 1])
            ans += 1
if sum([sum(f[i]) for i in range(n)]) == s:
    print(ans)
    for i in range(ans):
        for j in anslist[i]:
            print(j, end=" ")
        print()
else:
    print("-1")
