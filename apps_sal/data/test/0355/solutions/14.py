# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:01:05 2015

@author: gmarti
"""

import sys
from sys import stdin, stdout


chess = []
for i in range(8):
    chess.append([x for x in stdin.readline().rstrip().split()])


white_dist = []
black_dist = []

for i in range(8):
    for j in range(8):
        if chess[i][0][j] == "W":
            # check if black above
            is_black_above = False
            for k in range(0, i):
                if chess[k][0][j] == "B":
                    is_black_above = True
            if not is_black_above:
                white_dist.append(i)

        if chess[i][0][j] == "B":
            # check if white below
            is_white_below = False
            for k in range(i + 1, 8):
                if chess[k][0][j] == "W":
                    is_white_below = True
            if not is_white_below:
                black_dist.append(7 - i)


if (min(white_dist) <= min(black_dist)):
    stdout.write("A\n")
else:
    stdout.write("B\n")
