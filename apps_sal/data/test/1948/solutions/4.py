def prog():
    from sys import stdin
    from collections import deque
    n, x = map(int, stdin.readline().split())
    x -= 1
    d = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, stdin.readline().split())
        d[a - 1].append(b - 1)
        d[b - 1].append(a - 1)
    Alice = [1000000 for i in range(n)]
    Bob = [1000000 for i in range(n)]
    queue = deque()
    queue.append([0, 0])
    while queue:
        q1 = queue.popleft()
        Alice[q1[0]] = min(Alice[q1[0]], q1[1])
        for i, item in enumerate(d[q1[0]]):
            if Alice[item] == 1000000:
                queue.append([item, q1[1] + 1])
    queue.append([x, 0])
    while queue:
        q2 = queue.popleft()
        Bob[q2[0]] = min(Bob[q2[0]], q2[1])
        for i, item in enumerate(d[q2[0]]):
            if Bob[item] == 1000000:
                queue.append([item, q2[1] + 1])
    res = 0
    for i in range(n):
        A = Alice[i]
        if A > Bob[i]:
            if A > res:
                res = A
    print(2 * res)


prog()
