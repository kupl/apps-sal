n, queue_size = [int(x) for x in input().split()]

results = [-1 for _ in range(n)]

next_server_free_time = 1
queue = []
for idx in range(n):
    t, d = [int(x) for x in input().split()]

    while queue and next_server_free_time <= t:
        idx1, d1 = queue.pop(0)
        next_server_free_time += d1
        results[idx1] = next_server_free_time

    if next_server_free_time <= t:
        results[idx] = t + d
        next_server_free_time = t + d
    else:
        if len(queue) < queue_size:
            queue.append((idx, d))

while queue:
    idx, d = queue.pop(0)
    next_server_free_time += d
    results[idx] = next_server_free_time

print(' '.join([str(x) for x in results]))
