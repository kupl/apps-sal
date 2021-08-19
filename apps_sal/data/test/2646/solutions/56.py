from collections import deque
import sys


def bfs(graph, N, start):
    visited = [0] * N
    visited[start] = 1
    que = deque([start])
    while que:
        node = que.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = node + 1
                que.append(n)
    return visited


input = sys.stdin.readline


def main():
    (N, M) = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        (A, B) = map(lambda n: int(n) - 1, input().split())
        graph[A].append(B)
        graph[B].append(A)
    visited = bfs(graph, N, 0)[1:]
    if all(visited):
        print('Yes')
        print(*visited, sep='\n')
    else:
        print('No')


main()
