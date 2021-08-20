from collections import deque
K = int(input())
queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(K):
    ans = queue.popleft()
    x = ans % 10
    if x != 0:
        queue.append(ans * 10 + x - 1)
    queue.append(ans * 10 + x)
    if x != 9:
        queue.append(ans * 10 + x + 1)
print(ans)
