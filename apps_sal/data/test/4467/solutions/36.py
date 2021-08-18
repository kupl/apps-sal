n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
x = []
for i, j in a:
    x.append((i, j, 1))
for i, j in b:
    x.append((i, j, 2))
x.sort()
for i in range(2 * n):
    x[i] = (x[i][1], x[i][2])
ans = 0
while len(x):
    maxindex = 0
    maxvalue = -1
    flag = 0
    for i in range(len(x)):
        if x[i][0] > maxvalue and x[i][1] == 1:
            flag = 1
            maxvalue = x[i][0]
            maxindex = i
    if flag == 0:
        break
    flag = 0
    for i in range(maxindex + 1, len(x)):
        if (x[i][1] == 2):
            if (x[i][0] > maxvalue):
                ans += 1
                x.pop(i)
                x.pop(maxindex)
                flag = 1
                break
    if (flag == 0):
        x.pop(maxindex)
print(ans)
