import itertools
import math

n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
q = list(itertools.combinations(range(n), 2))
cnt = 0
for i in range(len(q)):
    ans = 0
    for j in range(d):
        ans += (x[q[i][0]][j] - x[q[i][1]][j])**2
    ans = math.sqrt(ans)
    if ans == int(ans):
        cnt += 1

print(cnt)
