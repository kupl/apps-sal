#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import deque
def main():
    N = int(input())
    Node = [set() for _ in range(N)]
    Edge = {}
    for i in range(N-1):
        a , b = list(map(int, input().split()))
        a-=1
        b-=1
        if b<a:
            a, b = b, a
        Edge[(a, b)]=i
        Node[a].add(b)
        Node[b].add(a)

    K = 0
    for i, x in enumerate(Node):
        if len(x)>K:
            K = len(x)
            top = i


    q = deque()
    seen = [False]*(N-1)
    used = [set() for _ in range(N)]
    q.append(top)
    while len(q)>0:
        cur = q.popleft()
        col = 1
        for i in Node[cur]:
            if cur>i:
                ed = (i, cur)
            else:
                ed = (cur, i)
            if seen[Edge[ed]]==False:
                while col in used[cur] or col in used[i]:
                    col+=1
                seen[Edge[ed]] = col
                used[cur].add(col)
                used[i].add(col)
                q.append(i)

    print(K)
    print(('\n'.join(map(str, seen))))

def __starting_point():
    main()

__starting_point()
