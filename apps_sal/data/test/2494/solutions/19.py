from collections import deque
k = int(input())
d = deque()
mat = []
for i in range(k):
    mat.append([])
dis = [10**18] * k
dis[1] = 0
for i in range(k):
    mat[i].append(((i + 1) % k, True))

    if (10 * i) % k != i:
        mat[i].append(((10 * i) % k, False))

d.append(1)
res = 0
while d:
    left = d.popleft()
    for neighbour, edge in mat[left]:
        distance = edge + dis[left]
        if dis[neighbour] > distance:
            dis[neighbour] = distance

            if edge == 0:
                d.appendleft(neighbour)
            else:
                d.append(neighbour)
print((dis[0] + 1))
