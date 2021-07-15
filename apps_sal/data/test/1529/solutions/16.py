import math
import re
from fractions import Fraction
from collections import Counter

class Task:
    sentences = []
    answer = []
    
    def __init__(self):
        self.sentences = ['' for _ in range(int(input()))]
        for i in range(len(self.sentences)):
            self.sentences[i] = input()

    def solve(self):
        sentences = self.sentences
        for current in sentences:
            matcherFirst = re.search('^miao\.', current) 
            matcherSecond = re.search('lala\.$', current)
            if matcherFirst != None and matcherSecond == None:
                self.answer += ["Rainbow's"]
                continue
            if matcherFirst == None and matcherSecond != None:
                self.answer += ["Freda's"]
                continue
            self.answer += ["OMG>.< I don't know!"]

    def printAnswer(self):
        for line in self.answer:
            print(line)

task = Task()
task.solve()
task.printAnswer()

