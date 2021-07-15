#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D_fix
# CreatedDate:  2020-09-15 21:36:31 +0900
# LastModified: 2020-09-15 22:19:28 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import deque


class BFS():
    def __init__(self, path, N):
        self.N = N
        self.color_path = [-1]*self.N
        self.path = path
        self.init = 1
        self.Q = deque([[0, self.init]])

    def forward(self):
        while self.Q:
            prev_path, u = self.Q.popleft()
            p_cnt = 1
            for cp, v in self.path[u]:
                if self.color_path[cp] == -1:
                    if prev_path == p_cnt:
                        p_cnt += 1
                    self.Q.append([p_cnt, v])
                    self.color_path[cp] = p_cnt
                    p_cnt += 1
#            print(self.color_path)

    def print_ans(self):
        self.color_path.pop(0)
        print((max(self.color_path)))
        for cp in self.color_path:
            print(cp)


def main():
    N = int(input())
    path = [[] for _ in range(N+1)]
    for i in range(1, N):
        a, b = list(map(int, input().split()))
        path[a].append([i, b])
        path[b].append([i, a])
    bfs = BFS(path, N)
    bfs.forward()
    bfs.print_ans()



def __starting_point():
    main()

__starting_point()
