tasks = list(map(int, input().split()))
max = tasks[0]
for i in range(1, 3, 1):
    if max < tasks[i]:
        max = tasks[i]
tasks.remove(max)
min = tasks[0]
if tasks[1] < min:
    min = tasks[1]
tasks.remove(min)
ans = max - min
print(ans)
