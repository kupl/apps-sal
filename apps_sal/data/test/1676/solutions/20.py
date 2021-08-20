import heapq
(n, b) = map(int, input().split())
ans = [-1 for i in range(n)]
queue = []
head = 0
size = 0
time = 0
for i in range(n):
    (t, d) = map(int, input().split())
    while size != 0 and time <= t:
        time += queue[head][0]
        ans[queue[head][1]] = time
        head += 1
        size -= 1
    if size == b:
        continue
    if size == 0 and time <= t:
        time = t + d
        ans[i] = time
        continue
    queue.append((d, i))
    size += 1
for i in range(head, len(queue)):
    time += queue[i][0]
    ans[queue[i][1]] = time
for x in ans:
    print(x, end=' ')
