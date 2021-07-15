from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

n_m = n // m
c = m * [0]
indices = [deque() for r in range(m)]

for i, ai in enumerate(a):
    r = ai % m
    c[r] += 1
    indices[r].append(i)

n_moves = 0
queue = deque()

for i in range(0, 2 * m):
    r = i % m
    
    while c[r] > n_m:
        queue.append((i, indices[r].pop()))
        c[r] -= 1
    
    while c[r] < n_m and queue:
        j, index = queue.popleft()
        indices[r].append(index)
        c[r] += 1
        a[index] += i - j
        n_moves += i - j

print(n_moves)
print(*a)
