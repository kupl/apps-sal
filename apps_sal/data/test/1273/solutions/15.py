import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
Edges = []
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    Edges.append((a - 1, b - 1))
Col = 0
for n in range(N):
    Col = max(Col, len(graph[n]))
Color = dict()
checked = [-1] * N
q = [0]
checked[0] = Col + 1
while q:
    qq = []
    for p in q:
        c = checked[p]
        t = 0
        for np in graph[p]:
            if checked[np] == -1:
                if t == c:
                    t += 1
                checked[np] = t
                Color[p, np] = t
                Color[np, p] = t
                t += 1
                qq.append(np)
    q = qq
print(Col)
for (a, b) in Edges:
    print(Color[a, b] + 1)
