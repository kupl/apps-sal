from sys import stdin
import sys
sys.setrecursionlimit(10**6)

n, k = list(map(int, stdin.readline().strip().split()))


def dfs(n):
    visited[n] = True
    while not visited[adj[n]]:
        n = adj[n]
        visited[n] = True


mod = 10**9 + 7
adj = [-1 for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(n):
    adj[i] = (i * k) % n
pairs = 0
for i in range(1, n):
    if not visited[i]:
        dfs(i)
        pairs += 1

if k == 1:
    print(pow(n, n, mod))
else:
    print(pow(n, pairs, mod))
