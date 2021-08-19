# -*- coding: utf-8 -*-
# @Date    : 2019-02-23 15:15:00
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import heapq
from collections import defaultdict
from sys import stdin

max_val = int(10e12)
min_val = int(-10e12)


def read_int(): return int(stdin.readline())
def read_ints(): return [int(x) for x in stdin.readline().split()]
def read_str(): return input()
def read_strs(): return [x for x in stdin.readline().split()]


n = int(input())
graph = defaultdict(set)
for x in range(n - 1):
    a, b = [int(x) for x in input().split()]
    graph[a].add((x, b))
    graph[b].add((x, a))

order = []
seen = set()
begin = 1
q = list(graph[begin])
heapq.heapify(q)
while q:
    t, node = heapq.heappop(q)
    if node in seen:
        continue
    seen.add(node)
    order.append(node)
    for neighbor in graph[node]:
        heapq.heappush(q, neighbor)
print(*order)
