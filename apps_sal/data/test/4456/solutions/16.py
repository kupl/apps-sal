from operator import itemgetter
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
inP = list(map(int, input().split()))
inQ = list(map(int, input().split()))


P = [None] * N
for i, p in enumerate(inP):
    P[p - 1] = i + 1

Q = [None] * N
for i, q in enumerate(inQ):
    Q[q - 1] = i + 1

NUM = []
for i, (p, q) in enumerate(zip(P, Q)):
    NUM.append((i, p, q))

graph = [-1] * (N + 1)
NUM.sort(key=itemgetter(2))
for i in range(N - 1):
    pre = NUM[i][1]
    fow = NUM[i + 1][1]
    graph[fow] = pre

NUM.sort(key=itemgetter(1))
Color = [-1] * (N + 1)
color = 0
MAX = 1
for (ind, p, q) in NUM:
    if Color[p] == -1 and p > MAX:
        color += 1
    tmp = p
    while tmp != -1 and Color[tmp] == -1:
        MAX = max(MAX, tmp)
        Color[tmp] = color
        tmp = graph[tmp]

if color >= K - 1:
    print("YES")
    ans = [None] * N
    for ind, p, q in NUM:
        c = Color[p]
        ans[ind] = chr(97 + min(c, 25))
    print("".join(ans))
else:
    print("NO")
