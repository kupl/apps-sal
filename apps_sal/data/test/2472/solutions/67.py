n = int(input())
task = []
for i in range(n):
    a, b = map(int, input().split())
    task.append([b, a])
sorted_task = sorted(task)
isOK = True
ans = 0
for i in range(n):
    ans += sorted_task[i][1]
    if ans > sorted_task[i][0]:
        isOK = False
        break
if isOK:
    print('Yes')
else:
    print('No')
