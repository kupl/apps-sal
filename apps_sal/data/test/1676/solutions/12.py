(n, b) = list(map(int, input().split()))
tasks = []
next_task = 0
time = 0
finish = [-1] * n
for i in range(n):
    (t, d) = list(map(int, input().split()))
    while tasks and next_task < len(tasks) and (time <= t):
        time += tasks[next_task][1]
        finish[tasks[next_task][0]] = time
        next_task += 1
    if len(tasks) - next_task < b:
        tasks.append((i, d))
    time = max(t, time)
while tasks and next_task < len(tasks):
    time += tasks[next_task][1]
    finish[tasks[next_task][0]] = time
    next_task += 1
print(*finish)
