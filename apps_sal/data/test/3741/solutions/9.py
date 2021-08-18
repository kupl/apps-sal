
from sys import stdin
import os
import sys
from atexit import register
from io import BytesIO
import itertools


def bfs(src, dest, adj):
    visited = [False for _ in range(len(adj))]
    visited[src] = True
    queue = [src]
    i = 1
    while len(queue) > 0:
        newq = []
        i += 1
        for node in queue:
            for vertex in adj[node]:
                if node == src and vertex == dest:
                    continue
                if not visited[vertex]:
                    newq.append(vertex)
                    visited[vertex] = True
                    if vertex == dest:
                        return i
        queue = newq
    return -1


def main():
    n = int(input())
    li = list(map(int, input().split()))
    binaries = [0] * n
    adj = [set() for _ in range(n)]
    for index, i in enumerate(li):
        binaries[index] = (bin(i)[2:].zfill(60))
    edges = set()
    for j in range(60):
        indexes = []
        for i in range(n):
            if binaries[i][j] == '1':
                indexes.append(i)
                if len(indexes) == 3:
                    print(3)
                    return
        if len(indexes) == 2:
            indexes.sort()
            edges.add(tuple(indexes))
            adj[indexes[0]].add(indexes[1])
            adj[indexes[1]].add(indexes[0])
    min_cycle = -1
    for li in edges:
        le = bfs(li[0], li[1], adj)
        if min_cycle == -1:
            min_cycle = le
        elif le > -1:
            min_cycle = min(min_cycle, le)
    print(min_cycle)


main()
