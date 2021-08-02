import sys
import math
import collections
import itertools
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N + 1)]

for _ in range(N - 1):
    a, b, c = list(map(int, input().split()))
    tree[a].append([b, c])
    tree[b].append([a, c])
Q, K = list(map(int, input().split()))

memo = [-1] * (N + 1)
q = collections.deque([K])
memo[K] = 0
while q:
    now = q.pop()
    for direct, cost in tree[now]:
        if memo[direct] == -1:
            memo[direct] = memo[now] + cost
            q.append(direct)
for _ in range(Q):
    a, b = list(map(int, input().split()))
    ans = memo[a] + memo[b]
    print(ans)
