"""
Codeforces April Fools Contest 2014 Problem D

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
answers = [1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0]

x = int(input())

# tests: 1 7 13 3 8 16 11 2 5 10 9 12- 12- 4 _ _
#if x not in [1,7,13,3,16,8,11,2,5,10] and x < 7: print(1/0)

print(answers[x-1])
