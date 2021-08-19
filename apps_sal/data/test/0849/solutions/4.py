import math
import re
from fractions import Fraction
from collections import Counter


class Task:
    (a, b, c, d) = (0, 0, 0, 0)
    answer = 0

    def __init__(self):
        (self.a, self.b, self.c, self.d) = [int(x) for x in input().split()]

    def solve(self):
        (a, b, c, d) = (self.a, self.b, self.c, self.d)
        p = a / b
        q = c / d
        x = (1 - p) * (1 - q)
        self.answer = p / (1 - x)

    def printAnswer(self):
        print(self.answer)


task = Task()
task.solve()
task.printAnswer()
