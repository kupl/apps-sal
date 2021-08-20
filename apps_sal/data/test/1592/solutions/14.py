n = int(input())
l = []
for i in range(n):
    (c, t) = list(map(int, input().split()))
    l.append((c, t))
queue = l[0][1]
z = queue
for i in range(1, n):
    queue = queue - min(l[i][0] - l[i - 1][0], queue)
    queue = queue + l[i][1]
    z = max(z, queue)
print(l[-1][0] + queue, z)
