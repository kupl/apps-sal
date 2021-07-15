"""
Codeforces Round 240 Div 1 Problem A

Author  : chaotic_iak
Language: Python 3.3.4
"""

class InputHandlerObject(object):
    inputs = []

    def getInput(self, n = 0):
        res = ""
        inputs = self.inputs
        if not inputs: inputs.extend(input().split(" "))
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

############################## SOLUTION ##############################
n,m = g()
n,m = int(n), int(m)
b = g()
a = [0] * n
for i in b:
    for j in range(int(i)-1, n):
        a[j] = i if a[j] == 0 else a[j]
print(" ".join(a))
