#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 07:28:11 2017

@author: fei
"""
n, m = [int(i) for i in input().split(' ')]
c = [int(i) for i in input().split(' ')]
chars = [[] for _ in range(n)]
for _ in range(m):
    p, q = [int(i) for i in input().split(' ')]
    p = p - 1
    q = q - 1
    chars[p].append(q)
    chars[q].append(p)


def dfs(i, nodes):
    if Visited[i]:
        return
    Visited[i] = True
    nodes.append(i)
    for j in chars[i]:
        dfs(j, nodes)


Visited = [False for i in range(n)]
Graph = []
C = 0
for i in range(n):
    if not Visited[i]:
        nodes = []
        nodes.append(i)
        tmp = 10000000000
        while len(nodes) > 0:
            u = nodes.pop()
            if Visited[u] == False:
                Visited[u] = True
                tmp = min(tmp, c[u])
                for j in chars[u]:
                    nodes.append(j)
        C += tmp
        Graph.append(nodes)

print(C)
