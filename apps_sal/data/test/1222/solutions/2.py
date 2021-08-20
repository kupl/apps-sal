from collections import deque
k = int(input())
maximum = 3234566667
lst = list(range(1, 10))
que = deque()
for i in range(1, 10):
    que.append(i)
    while que:
        now = que.pop()
        if now >= maximum:
            continue
        for j in range(max(0, now % 10 - 1), min(10, now % 10 + 2)):
            lst.append(now * 10 + j)
            que.append(now * 10 + j)
lst.sort()
print(lst[k - 1])
