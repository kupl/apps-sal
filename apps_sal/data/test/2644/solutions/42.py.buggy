import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
p = list(map(int, input().split()))
pos = [0] * n
seen = [False] * n
ans = []
for i in range(n):
    p[i] -= 1
    pos[p[i]] = i

for i in range(n):
    if pos[i] == i:
        continue
    for j in range(pos[i], i, -1):
        if seen[j]:
            print(-1)
            return
        seen[j] = True
        p[j], p[j - 1] = p[j - 1], p[j]
        pos[p[j]], pos[p[j - 1]] = j, j - 1
        ans.append(j)
if len(ans) == n - 1:
    print(*ans, sep="\n")
else:
    print(-1)
