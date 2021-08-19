from collections import deque
K = int(input())
deq = deque([(1, 1)])
history = set()
while True:
    to = deq.popleft()
    if to[0] == 0:
        print(to[1])
        break
    elif to[0] not in history:
        history.add(to[0])
        deq.appendleft((to[0] * 10 % K, to[1]))
        deq.append((to[0] + 1, to[1] + 1))
