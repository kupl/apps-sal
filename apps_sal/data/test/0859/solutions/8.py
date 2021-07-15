__author__ = 'neki'

import sys

#sys.stdin = open("wifi.in", "r")

def outcome(command):
    pos = 0
    for i in command:
        if i == "+": pos += 1
        elif i == "-": pos -= 1
        else: print("Error")
    return pos

def computeFinishes(k):
    nonlocal finish, recCommand, xCom, nSol

    if k >= len(xCom): #solution
        nSol += 1
        #print(k)
        solCom = recCommand[:]
        for i in range(len(xCom)):
            if xCom[i] == 1:
                solCom[i] = "+"
            if xCom[i] == 2:
                solCom[i] = "-"
        #print(xCom)
        #print(solCom)
        finish[outcome(solCom)] += 1
        return
    if recCommand[k] == "?":
        for j in range(1, 3):
            xCom[k] = j
            computeFinishes(k+1)
    else:
        computeFinishes(k+1)
    xCom[k] = 0

sentCommand1 = str(input())
recCommand1 = str(input())

sentCommand = ["A"] * len(sentCommand1)
recCommand = ["B"] * len(recCommand1)

for i in range(len(sentCommand1)):
    sentCommand[i] = sentCommand1[i]
    recCommand[i] = recCommand1[i]

#print(sentCommand)
#print(recCommand)

#print("Solutions")
sentFinish = outcome(sentCommand)
finish = {}
for i in range(-10, 11):
    finish[i] = 0

xCom = [0] * len(recCommand)

nSol = 0
computeFinishes(0)
result = finish[sentFinish] / nSol

print("{result:.12f}".format(result=result))

