import queue
K = int(input())
q = queue.Queue()
for i in range(1, 10):
    q.put(i)

for _ in range(K):
    x = q.get()
    r = x % 10
    y = 10 * x + r
    if r != 0:
        q.put(y - 1)
    q.put(y)
    if r != 9:
        q.put(y + 1)

print(x)
