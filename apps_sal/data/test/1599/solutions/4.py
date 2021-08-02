import math
import re
from fractions import Fraction
from collections import Counter


class Task:
    s = ''
    queries = []
    answer = []

    def __init__(self):
        self.s = input()
        self.queries = [[] for _ in range(int(input()))]
        for i in range(len(self.queries)):
            self.queries[i] = [int(x) for x in input().split()]

    def solve(self):
        s, queries = self.s, self.queries
        d = [0] * len(s)
        d[0] = 1 if s[0] == s[1] else 0
        for i in range(1, len(d) - 1):
            d[i] = d[i - 1] + (s[i + 1] == s[i])
        d[-1] = d[-2]

        for current in queries:
            localAnswer = d[current[1] - 2]
            localAnswer -= d[current[0] - 2] if current[0] >= 2 else 0
            self.answer += [localAnswer]

    def printAnswer(self):
        for x in self.answer:
            print(x)


task = Task()
task.solve()
task.printAnswer()
