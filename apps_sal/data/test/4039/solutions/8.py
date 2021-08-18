from sys import stdin, stdout
import math

N, r = [int(x) for x in stdin.readline().split()]

visited = [0] * N

a = [0] * N
b = [0] * N

pos = 0

for i in range(N):
    arr = [int(x) for x in stdin.readline().split()]
    a[i] = arr[0]
    b[i] = arr[1]

    if b[i] >= 0:
        pos += 1

for i in range(pos):
    idx = -1
    start = 0
    gain = -50000
    for j in range(N):
        if visited[j] == 1 or b[j] < 0:
            continue

        if b[j] > gain and r >= a[j]:
            gain = b[j]
            idx = j
            start = a[j]
        elif b[j] == gain and r >= a[j]:
            if a[j] > start:
                idx = j
                start = a[j]

    if idx == -1:
        print('NO')
        quit()
    else:
        visited[idx] = 1
        r += b[idx]


tmp = []
for i in range(N):
    if visited[i] == 1 or b[i] >= 0:
        continue
    tmp.append((a[i], b[i], i))

tmp.sort(key=lambda e: (e[0] + e[1], e[0]), reverse=True)

for i in range(len(tmp)):
    require = tmp[i][0]
    bias = tmp[i][1]

    if r >= require:
        r += bias
    else:
        print('NO')
        quit()


if r < 0:
    print('NO')
    quit()

print('YES')
