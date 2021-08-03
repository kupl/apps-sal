from collections import deque
k = int(input())
que = deque(list(range(1, 10)))
for i in range(k):
    a = que.popleft()
    b = a % 10
    l = 10 * a + b - 1
    c = l + 1
    r = c + 1
    if b != 0:
        que.append(l)
    que.append(c)
    if b != 9:
        que.append(r)
print(a)
