from collections import deque
N = int(input())
f = [[] for i in range(N)]
for i in range(N - 1):
    (a, b, c) = map(int, input().split())
    f[a - 1].append([b - 1, c])
    f[b - 1].append([a - 1, c])
d = deque()
s = [-1] * N
(Q, K) = map(int, input().split())
d.append(K - 1)
s[K - 1] = 0
while len(d) > 0:
    z = d.popleft()
    for (i, j) in f[z]:
        if s[i] == -1:
            s[i] = j + s[z]
            d.append(i)
for i in range(Q):
    (x, y) = map(int, input().split())
    print(s[x - 1] + s[y - 1])
