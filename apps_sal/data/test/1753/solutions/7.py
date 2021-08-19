import math
(n, m) = list(map(int, input().split()))
hs = []
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    hs.append((min(a, b), max(a, b)))
used = [0] * n
placed = [[] for _ in range(n)]
for (a, b) in hs:
    placed[a].append(b * n + used[b])
    used[b] += 1
for i in range(n):
    print(max(1, used[i]) + len(placed[i]))
    for j in range(max(1, used[i])):
        print(i * n + j + 1, i + 1)
    for j in placed[i]:
        print(j + 1, i + 1)
