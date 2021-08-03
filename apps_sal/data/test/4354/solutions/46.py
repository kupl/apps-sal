import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s = []
for _ in range(N):
    a, b = map(int, input().split())
    s.append((a, b))

g = []
for _ in range(M):
    c, d = map(int, input().split())
    g.append((c, d))

ans = []
for i in range(N):
    a, b = s[i]
    i_ans = -1
    tmp = float("inf")
    for j in range(M):
        c, d = g[j]
        dist = abs(c - a) + abs(d - b)
        # print(i, j, dist)
        if dist < tmp:
            i_ans = j
            tmp = dist
    ans.append(i_ans)

for a in ans:
    print(a + 1)
