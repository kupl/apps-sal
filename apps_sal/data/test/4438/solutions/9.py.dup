from sys import stdin
n = int(stdin.readline().strip())
s = []
s1 = []
for i in range(n):
    a, b = list(map(int, stdin.readline().strip().split()))
    s.append((a, b))
    s1.append((b, a))
s.sort()
s1.sort(reverse=True)
mt = dict()
for i in s:
    if i[0] <= i[1]:
        if i[1] in mt:
            mt[i[1]].append(i)
        else:
            mt.update({i[1]: [i]})
for i in s1:
    if i[1] > i[0]:
        if i[1] in mt:
            mt[i[1]].append((i[1], i[0]))
        else:
            mt.update({i[1]: [(i[1], i[0])]})
v = [[(0, 0)]]
k = list(mt.keys())
k.sort()
for i in k:
    v.append(mt[i])
n = len(v)
dp = [[-1, -1] for i in range(n)]
dp[0][0] = 0
dp[0][1] = 0
dist = [0 for i in range(n)]
for i in range(1, n):
    x = 0
    for j in range(1, len(v[i])):
        x += abs(v[i][j][0] - v[i][j - 1][0]) + abs(v[i][j][1] - v[i][j - 1][1])
    dist[i] = x
for i in range(1, n):
    dp[i][1] = dist[i] + (min(dp[i - 1][1] + abs(v[i][0][0] - v[i - 1][-1][0]) + abs(v[i][0][1] - v[i - 1][-1][1]), dp[i - 1][0] + abs(v[i][0][0] - v[i - 1][0][0]) + abs(v[i][0][1] - v[i - 1][0][1])))
    dp[i][0] = dist[i] + (min(dp[i - 1][1] + abs(v[i][-1][0] - v[i - 1][-1][0]) + abs(v[i][-1][1] - v[i - 1][-1][1]), dp[i - 1][0] + abs(v[i][-1][0] - v[i - 1][0][0]) + abs(v[i][-1][1] - v[i - 1][0][1])))
print(min(dp[-1]))
