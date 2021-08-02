import math
import re
from fractions import Fraction
from collections import Counter


class Task:
    n = 0
    answer = 0

    def __init__(self):
        self.n = input()

    def solve(self):
        n = self.n
        self.answer = max(int(n), int(n[:-2] + n[-1]), int(n[:-1]))

    def printAnswer(self):
        print(self.answer)


task = Task()
task.solve()
task.printAnswer()
