from collections import deque


def solve(X):
    waiting = deque()
    res = [None] * len(X)
    t = 0
    X.append((10000, 10000))
    for (i, (l, r)) in enumerate(X):
        while waiting and t < l:
            (j, b) = waiting.popleft()
            if t <= b:
                res[j] = t
                t += 1
            else:
                res[j] = 0
        waiting.append((i, r))
        t = l
    return res


T = int(input())
for _ in range(T):
    n = int(input())
    X = [tuple(map(int, input().split())) for _ in range(n)]
    res = solve(X)
    print(' '.join(map(str, res)))
