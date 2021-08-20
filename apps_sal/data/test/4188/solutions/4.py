"""
Codeforces April Fools Contest 2014 Problem D

Author  : chaotic_iak
Language: Python 3.3.4
"""


class InputHandlerObject(object):
    inputs = []

    def getInput(self, n=0):
        res = ''
        inputs = self.inputs
        if not inputs:
            inputs.extend(input().split(' '))
        if n == 0:
            res = inputs[:]
            inputs[:] = []
        while n > len(inputs):
            inputs.extend(input().split(' '))
        if n > 0:
            res = inputs[:n]
            inputs[:n] = []
        return res


InputHandler = InputHandlerObject()
g = InputHandler.getInput
answers = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
x = int(input())
print(answers[x - 1])
