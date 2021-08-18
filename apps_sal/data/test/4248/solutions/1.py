"""
Codeforces April Fools Contest 2014 Problem G

Author  : chaotic_iak
Language: Python 3.3.4
"""


class InputHandlerObject(object):
    inputs = []

    def getInput(self, n=0):
        res = ""
        inputs = self.inputs
        if not inputs:
            inputs.extend(input().split(" "))
        if n == 0:
            res = inputs[:]
            inputs[:] = []
        while n > len(inputs):
            inputs.extend(input().split(" "))
        if n > 0:
            res = inputs[:n]
            inputs[:n] = []
        return res


InputHandler = InputHandlerObject()
g = InputHandler.getInput

n = int(input())
sum = 0
for i in range(n):
    nx, ny = g()
    sum += float(ny)
print(5 + (sum / n))
