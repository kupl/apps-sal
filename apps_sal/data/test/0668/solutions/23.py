from collections import deque

n, a = int(input()), list(map(int, input().split()))
a_sorted = sorted([a[i], i + 1] for i in range(1, n))
messages = []
queue = deque([[a[0], 1]])
while a_sorted and queue:
    cur = queue.popleft()
    while cur[0] and a_sorted:
        recipient = a_sorted.pop()
        messages.append((cur[1], recipient[1]))
        queue.append(recipient)
        cur[0] -= 1
if a_sorted:
    print(-1)
else:
    print(len(messages))
    for message in messages:
        print(*message)

