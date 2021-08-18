n = int(input())
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])
arr.sort(key=lambda x: x[0])
queue_size = 0
time = 0
max_queue_size = 0
last_time = 0
for t, c in arr:
    sent = t - last_time
    queue_size = max(0, queue_size - sent)
    queue_size += c
    time = t
    max_queue_size = max(max_queue_size, queue_size)
    last_time = time
print(time + queue_size, max_queue_size)
