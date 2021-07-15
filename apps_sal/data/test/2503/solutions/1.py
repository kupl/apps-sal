import sys

#縦k、横kのマスに移動させて考える
n, k = map(int, sys.stdin.readline().strip().split())
x = []
y = []
mx = []
my = []
for _ in range(n):
    xx, yy, c = sys.stdin.readline().strip().split()
    xx = int(xx)
    yy = int(yy)
    if c == 'W':
        xx += k
    xx %= 2 * k
    yy %= 2 * k
    if xx >= k:
        if yy >= k:
            x.append(xx - k)
            y.append(yy - k)
        else:
            mx.append(xx - k)
            my.append(yy)
    else:
        if yy >= k:
            mx.append(xx)
            my.append(yy - k)
        else:
            x.append(xx)
            y.append(yy)

graph = [[0 for _ in range(k)] for __ in range(k)]

#累積和
#lx + lmx = n
lx = len(x)
graph[0][0] += lx
for i in range(lx):
    graph[x[i]][0] -= 1
    graph[0][y[i]] -= 1
    graph[x[i]][y[i]] += 2

lmx = len(mx)
graph[0][0] -= lmx
for i in range(lmx):
    graph[mx[i]][0] += 1
    graph[0][my[i]] += 1
    graph[mx[i]][my[i]] -= 2

for i in graph:
    for j in range(k-1):
        i[j+1] += i[j]

for i in range(k):
    for j in range(k-1):
        graph[j+1][i] += graph[j][i]

#最大値、最小値を取得
big = max([max(i) for i in graph]) + lmx
small = min([min(i) for i in graph]) - lx

if big + small >= 0:
    print(big)
else:
    print(-small)
