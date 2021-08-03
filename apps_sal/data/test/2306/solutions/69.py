import heapq
n = int(input())
inf = 10000000000000
ans = [[-1, -1] for i in range(n)]
ans[-1][1], ans[0][0] = 0, 0
t = list(map(int, input().split()))
v = list(map(int, input().split()))
v2 = []
for i in range(n):
    heapq.heappush(v2, (v[i], i))


def next(y, wh):
    nonlocal ans, n
    ansi = inf
    if wh:
        r1, r2 = range(y[1] - 1, -1, -1), range(y[1], n)
    else:
        r1, r2 = range(y[1], -1, -1), range(y[1] + 1, n)
    now = 0
    for j in r1:
        if ans[j][1] != -1:
            ansi = min(ansi, ans[j][1] + now)
        now += t[j]
        if ans[j][0] != -1:
            ansi = min(ansi, ans[j][0] + now)
    now = 0
    for j in r2:
        if ans[j][0] != -1:
            ansi = min(ansi, ans[j][0] + now)
        now += t[j]
        if ans[j][1] != -1:
            ansi = min(ansi, ans[j][1] + now)
    if wh:
        ans[y[1]][0] = min(ansi, y[0])
        ans[y[1] - 1][1] = ans[y[1]][0]
    else:
        ans[y[1]][1] = min(ansi, y[0])
        ans[y[1] + 1][0] = ans[y[1]][1]


for i in range(n):
    y = heapq.heappop(v2)
    if ans[y[1]][0] == -1:
        next(y, True)
    if ans[y[1]][1] == -1:
        next(y, False)
answer = 0
for i in range(n):
    h = min((t[i] + sum(ans[i])) / 2, v[i])
    answer += ((h**2 - ans[i][0]**2) / 2)
    answer += ((h**2 - ans[i][1]**2) / 2)
    answer += (h * (t[i] + sum(ans[i]) - 2 * h))
print(answer)
