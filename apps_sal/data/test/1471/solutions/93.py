from collections import deque, defaultdict
n = int(input())
l = []
dc = [-1] * n
d = defaultdict(list)
for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    w %= 2
    d[u - 1].append([v - 1, w])
    d[v - 1].append([u - 1, w])
# print(d)

Q = deque()
Q.append(0)
dc[0] = 0
while Q:
    q = Q.pop()

    for v, w in d[q]:
        if dc[v] == -1:
            dc[v] = (dc[q] + w) % 2
            Q.append(v)

for i in dc:
    print(i)
