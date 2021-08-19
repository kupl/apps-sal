from collections import deque
K = int(input())
q = deque([i for i in range(1, 10)])
for _ in range(K - 1):
    x = deque.popleft(q)
    a = x % 10
    if a != 0 and a != 9:
        deque.append(q, x * 10 + a - 1)
        deque.append(q, x * 10 + a)
        deque.append(q, x * 10 + a + 1)
    elif a == 0:
        deque.append(q, x * 10)
        deque.append(q, x * 10 + 1)
    else:
        deque.append(q, x * 10 + 8)
        deque.append(q, x * 10 + 9)
print(deque.popleft(q))
