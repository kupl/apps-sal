#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
triple = []
indexes = [[] for _ in range(n)]
cnt = [0] * n
abc = []
for i in range(n-2):
    a, b, c = [int(item)-1 for item in input().split()]
    abc.append((a, b, c))
    indexes[a].append(i)
    indexes[b].append(i)
    indexes[c].append(i)
    cnt[a] += 1
    cnt[b] += 1
    cnt[c] += 1
tmp = cnt[:]

ans = []
node = cnt.index(1)
visited = [0] * (n - 2)
nxt = indexes[node][0]
while True:
    for item in indexes[node]:
        if visited[item]:
            continue
        nxt = item
        visited[nxt] = 1
    a, b, c = abc[nxt]
    if cnt[a] == 1 and cnt[b] == 1 and cnt[c] == 1:
        break
    ans.append(node+1)
    cnt[a] -= 1
    cnt[b] -= 1
    cnt[c] -= 1
    if cnt[a] == 1:
        node = a
    elif cnt[b] == 1:
        node = b
    elif cnt[c] == 1:
        node = c

for item in abc[nxt]:
    if tmp[item] == 3:
        ans.append(item + 1)
for item in abc[nxt]:
    if tmp[item] == 2:
        ans.append(item + 1)
for item in abc[nxt]:
    if tmp[item] == 1:
        ans.append(item + 1)

print(" ".join([str(item) for item in ans]))
