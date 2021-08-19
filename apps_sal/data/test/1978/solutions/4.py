import sys


def input():
    return sys.stdin.readline()[:-1]


n = int(input())
s = [input() for _ in range(n)]
d = [[10 ** 30 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == '1':
            d[i][j] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
m = int(input())
p = list(map(int, input().split()))
ans = [p[0]]
cur = 1
while cur < m - 1:
    if ans[-1] == p[cur + 1]:
        ans.append(p[cur])
    elif d[ans[-1] - 1][p[cur] - 1] + d[p[cur] - 1][p[cur + 1] - 1] > d[ans[-1] - 1][p[cur + 1] - 1]:
        ans.append(p[cur])
    cur += 1
ans.append(p[-1])
print(len(ans))
print(*ans)
