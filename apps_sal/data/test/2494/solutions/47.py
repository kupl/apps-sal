from collections import deque

def solve(K):
    checked = [99999999999] * (K + 1)
    queue = deque()
    queue.append((1, 1))
    checked[1] = 1
    while queue:
        x, n = queue.popleft()
        if x == 0:
            return n
        _ = (x * 10) % K 
        if n < checked[_]:
            queue.appendleft((_, n))
            checked[_] = n
        _ = (x + 1) % K 
        if n + 1 < checked[_]:
            queue.append((_, n + 1))
            checked[_] = n + 1
    return None

K = int(input())
print((solve(K)))


