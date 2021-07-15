
import os
import sys
import functools
import collections
import itertools


class Solution:
    def __init__(self):
        self.M = 0
        self.N = 0
        self.notes = None

    def readInput(self):
        self.N, self.M = [int(x) for x in input().split()]
        self.notes = []
        for i in range(self.M):
            di, hi = [int(x) for x in input().split()]
            self.notes.append((di, hi))
    def readMockInput(self):
        pass

    def solve(self):

        if self.notes[0][0] > 1:
            self.notes = [(1, sum(self.notes[0])-1)] + self.notes
        if self.notes[-1][0] < self.N:
            self.notes.append((self.N, self.notes[-1][1]+self.N-self.notes[-1][0]))

        res = max([x[1] for x in self.notes])
        for i in range(1, len(self.notes)):
            d1, h1 = self.notes[i-1]
            d2, h2 = self.notes[i]
            if abs(h1-h2) > abs(d1-d2):
                print('IMPOSSIBLE')
                return
            res = max(res, (abs(d1-d2)+h1+h2) // 2)

        print(res)




s = Solution()
s.readInput()
# s.readMockInput()
s.solve()
