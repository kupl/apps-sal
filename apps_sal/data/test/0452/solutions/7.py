import re
import itertools
from collections import Counter, deque
from fractions import gcd


class Task:
    (p, q) = (0, 0)
    a = []
    answer = ''

    def getData(self):
        (self.p, self.q) = [int(x) for x in input().split(' ')]
        input()
        self.a = [int(x) for x in input().split(' ')]

    def solve(self):
        (p, q) = self.toFraction(self.a)
        if self.p * q == self.q * p:
            self.answer = 'YES'
        else:
            self.answer = 'NO'

    def toFraction(self, a):
        if len(a) == 1:
            return (a[0], 1)
        (q, p) = self.toFraction(a[1:])
        d = gcd(a[0] * q + p, q)
        return ((a[0] * q + p) // d, q // d)

    def printAnswer(self):
        print(self.answer)


task = Task()
task.getData()
task.solve()
task.printAnswer()
