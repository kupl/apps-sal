import re
import itertools
from collections import Counter, deque


class Task:
    numbers = []
    answer = set()

    def getData(self):
        input()
        self.numbers = [int(x) for x in input().split(' ')]

    def solve(self):
        firstZero = False
        secondZero = False
        for x in self.numbers:
            if x % 100 == 0:
                self.answer.add(x)
                continue
            if x % 10 == 0 and x > 0 and (firstZero == False):
                self.answer.add(x)
                firstZero = True
                continue
            if 0 < x < 10 and secondZero == False:
                self.answer.add(x)
                secondZero = True
        if firstZero == False and secondZero == False:
            for x in self.numbers:
                if x != 0 and x != 100:
                    self.answer.add(x)
                    break

    def printAnswer(self):
        print(len(self.answer))
        print(re.sub('[\\{\\},]', '', str(self.answer)))


task = Task()
task.getData()
task.solve()
task.printAnswer()
