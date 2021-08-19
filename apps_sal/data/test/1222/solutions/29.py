import queue


def resolve():
    n = int(input())
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)
    for _ in range(n):
        x = q.get()
        if x % 10 != 0:
            q.put(10 * x + x % 10 - 1)
        q.put(10 * x + x % 10)
        if x % 10 != 9:
            q.put(10 * x + x % 10 + 1)
    print(x)


resolve()
