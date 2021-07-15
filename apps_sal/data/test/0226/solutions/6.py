import math
from random import random

def getInt():
    return(int(input()))

def getInts():
    line = input().split()
    return [int(l) for l in line]

def getFloat():
    return(float(input()))

def getFloats():
    line = input().split()
    return [float(l) for l in line]

def getStrings():
    line = input().split()
    return(line)


N = getInt()
values = getInts()

nConsidered = 0
#                nC, nO
bestForChooserSoFar = [0, 0]

for i in range(len(values)):
    v = values[len(values) - i - 1]
    qsIfTaken = [v + bestForChooserSoFar[1], bestForChooserSoFar[0]]
    qsIfGiven = [bestForChooserSoFar[0], v + bestForChooserSoFar[1]]

    if(qsIfTaken[0] >= qsIfGiven[0]):
        bestForChooserSoFar = qsIfTaken
    else:
        bestForChooserSoFar = qsIfGiven

print(str(bestForChooserSoFar[1]) + ' ' + str(bestForChooserSoFar[0]))
