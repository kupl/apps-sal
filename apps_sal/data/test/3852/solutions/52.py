n = int(input())
arr = list(map(int, input().split()))
arr = [[arr[i], i + 1] for i in range(n)]
mins = 10 ** 18
minpos = 0
maxs = -10 ** 18
maxpos = 0
for i in range(n):
    a = arr[i][0]
    if a < mins:
        mins = a
        minpos = i + 1
    if maxs < a:
        maxs = a
        maxpos = i + 1
ans = []
if maxs <= 0:
    flag = False
elif mins >= 0:
    flag = True
elif maxs >= abs(mins):
    flag = True
    for i in range(n):
        arr[i][0] += maxs
        ans.append([maxpos, arr[i][1]])
else:
    flag = False
    for i in range(n):
        arr[i][0] += mins
        ans.append([minpos, arr[i][1]])
if flag == True:
    for i in range(1, n):
        ans.append([i, i + 1])
else:
    for i in range(n, 1, -1):
        ans.append([i, i - 1])
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
