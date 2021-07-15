n = int(input())
queues = list(map(int, input().split()))
mns = [None] * n
for num in range(n):
    mns[num] = list(map(int, input().split()))
times = [None] * n
for num in range(n):
    time = 0
    for i in range(queues[num]):
        time += mns[num][i] * 5 + 15
    times[num] = time
print(min(times))
