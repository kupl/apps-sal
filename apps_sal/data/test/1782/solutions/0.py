import re
import itertools
from collections import Counter, deque


class Task:
    n, k = 0, 0
    answer = []

    def getData(self):
        self.n, self.k = [int(x) for x in input().split(' ')]

    def solve(self):
        n, k = self.n, self.k
        if n < 3 * k:
            self.answer = '-1'
            return

        keeper = 1
        while keeper < k:
            self.answer += [keeper, keeper, keeper + 1]
            self.answer += [keeper, keeper + 1, keeper + 1]
            keeper += 2
        if keeper > k:
            self.answer += [k] * (n - len(self.answer))
            return
        else:
            self.answer += [keeper] * (n - len(self.answer))
            self.answer[-1] = 1
            self.answer[3] = keeper

    def printAnswer(self):
        print(re.sub(r'[\[\],]', '', str(self.answer)))


task = Task()
task.getData()
task.solve()
task.printAnswer()
