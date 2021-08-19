from array import array
from collections import deque
3


def dfs():
    while len(queue) != 0:
        s = queue.popleft()
        (i, j) = s
        for (ni, nj) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if ni in range(0, n) and nj in range(0, m):
                c = ni * m + nj
                fl = data[c]
                if e == (ni, nj) and fl == 1:
                    return True
                elif fl == 0:
                    data[c] = 1
                    queue.append((ni, nj))
    return False


[n, m] = list(map(int, input().split()))
data = array('B')
for i in range(0, n):
    data.extend([0 if x == '.' else 1 for x in input()])
[si, sj] = list(map(int, input().split()))
[ei, ej] = list(map(int, input().split()))
e = (ei - 1, ej - 1)
queue = deque()
queue.append((si - 1, sj - 1))
print('YES' if dfs() else 'NO')
