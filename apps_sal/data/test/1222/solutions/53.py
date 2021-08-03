from queue import Queue as Q
k = int(input())
q = Q()
[q.put(i) for i in range(1, 10)]

for i in range(k):
    x = q.get()
    if x % 10 != 0:
        q.put(10 * x + (x % 10) - 1)
    q.put(10 * x + (x % 10))
    if x % 10 != 9:
        q.put(10 * x + (x % 10) + 1)

print(x)
