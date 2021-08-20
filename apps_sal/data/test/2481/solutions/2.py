(h, w) = map(int, input().split())
c = []
for i in range(10):
    c.append(list(map(int, input().split())))
a = []
for i in range(h):
    a.append(list(map(int, input().split())))
cost = [float('inf') for i in range(10)]
flag = [False for i in range(10)]
cost[1] = 0
test = [1]
while test:
    num = test.pop(0)
    flag[num] = True
    for i in range(10):
        cost[i] = min(cost[i], cost[num] + c[i][num])
    temp = [[cost[i], i] for i in range(10)]
    temp.sort()
    for i in range(10):
        if flag[temp[i][1]] == True:
            continue
        else:
            test.append(temp[i][1])
            break
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue
        else:
            ans += cost[a[i][j]]
print(ans)
