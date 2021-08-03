from collections import deque


N, Q = list(map(int, input().split()))
t = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    t[a].append(b)
    t[b].append(a)

score = [0] * (N + 1)
for i in range(Q):
    p, x = list(map(int, input().split()))
    score[p] += x

is_read = [False] * (N + 1)
d = deque()
d.append(1)

while len(d) != 0:
    now = d.popleft()
    is_read[now] = True
    for c in t[now]:
        if is_read[c]:
            continue
        score[c] += score[now]
        d.append(c)
print((" ".join(map(str, score[1:]))))
