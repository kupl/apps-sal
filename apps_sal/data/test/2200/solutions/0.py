"""
Codeforces Round 240 Div 1 Problem B

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

n, a, b = g()
n, a, b = int(n), int(a), int(b)
c = [int(x) for x in g()]
r = []
for i in c:
    r.append(str(((i * a) % b) // a))
print(" ".join(r))
