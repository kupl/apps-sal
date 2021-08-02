import sys
input = sys.stdin.readline

N = int(input())
edges = []
for _ in range(N - 1):
    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    if u > v:
        u, v = v, u
    edges.append((u, v))

numV = 0
for i in range(N):
    numV += (i + 1) * (N - i)

numE = 0
for u, v in edges:
    numE += (u + 1) * (N - v)

ans = numV - numE
print(ans)
