n, k = map(int, input().split())
ids = input().split()
queue = []
for i in ids:
    if len(queue) < k and i not in queue:
        queue.insert(0, i)
    elif len(queue) >= k and i not in queue:
        del queue[-1]
        queue.insert(0, i)
print(len(queue))
print(' '.join(queue))
