# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/7/20

reverse thinking of merging instead of split

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class Node:
    val = None

    def __init__(self, val):
        self.val = val
        self.left = Node
        self.right = None


def solve(W, H, N, A):
    xs = [0] + [v for t, v in A if t == 0] + [W]
    ys = [0] + [v for t, v in A if t == 1] + [H]
    xs.sort()
    ys.sort()

    xlist = Node(0)
    h = xlist
    xnodes = {0: h}
    maxw = max([xs[i+1] - xs[i] for i in range(len(xs)-1)] or [0])
    maxh = max([ys[i+1] - ys[i] for i in range(len(ys)-1)] or [0])
    for v in xs[1:]:
        n = Node(v)
        xnodes[v] = n
        h.right = n
        n.left = h
        h = n
        
    ylist =  Node(0)
    h = ylist
    ynodes = {0: h}
    for v in ys[1:]:
        n = Node(v)
        ynodes[v] = n
        h.right = n
        n.left = h
        h = n
    
    ans = []
    maxarea = maxh * maxw
    for t, v in reversed(A):
        ans.append(maxarea)
        if t == 0:
            node = xnodes[v]
            w = node.right.val - node.left.val
            maxw = max(maxw, w)
        else:
            node = ynodes[v]
            h = node.right.val - node.left.val
            maxh = max(maxh, h)
        node.left.right = node.right
        node.right.left = node.left
        maxarea = maxh * maxw
    
    return ans[::-1]
    
    
def solve2(W, H, N, A):
    ws = [(-W, 0, W)]
    hs = [(-H, 0, H)]
    iw, ih = set(), set()
    ans = []
    
    xs, ys = [0, W], [0, H]
    for t, v in A:
        if t == 0:
            bisect.insort_left(xs, v)
            i = bisect.bisect_left(xs, v)
            l, m, r = xs[i-1], xs[i], xs[i+1]
            iw.add((l-r, l, r))
            heapq.heappush(ws, (l - m, l, m))
            heapq.heappush(ws, (m - r, m, r))
            while ws[0] in iw:
                heapq.heappop(ws)
        else:
            bisect.insort(ys, v)
            i = bisect.bisect_left(ys, v)
            l, m, r = ys[i-1], ys[i], ys[i+1]
            ih.add((l-r, l, r))
            heapq.heappush(hs, (l - m, l, m))
            heapq.heappush(hs, (m - r, m, r))
            while hs[0] in ih:
                heapq.heappop(hs)
        w, h = ws[0], hs[0]
        ans.append(w[0] * h[0])
        
    return ans


W, H, N = map(int,input().split())
A = []
for i in range(N):
    a, b = input().split()
    c = 0 if a == 'V' else 1
    A.append((c, int(b)))

print('\n'.join(map(str, solve(W, H, N, A))))
