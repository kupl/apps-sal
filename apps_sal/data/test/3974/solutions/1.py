import math
import re
from fractions import Fraction
from collections import Counter

class Task:
    signs = ''
    answer = 0
    
    def __init__(self):
        self.signs = input()

    def solve(self):
        counter = 0
        leftBound, rightBound = 0, 0
        for x in self.signs:
            counter += 1 if x == '+' else -1
            leftBound = min(leftBound, counter)
            rightBound = max(rightBound, counter)
        self.answer = rightBound - leftBound

    def printAnswer(self):
        print(self.answer)

task = Task()
task.solve()
task.printAnswer()

