import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n - 1)]
    graph = [[] for i in range(n + 1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)
    if len(graph[x]) == 1 or n == 1:
        print("Ayush")
        continue
    if n % 2:
        print("Ashish")
    else:
        print("Ayush")
