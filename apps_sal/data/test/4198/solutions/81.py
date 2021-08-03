import math


def calcMaxNum(minCandidate: int, maxCandidate: int, A, B, X):
    if(A == 0 and B == 0):
        print(10**9)
        return
    if(maxCandidate >= 10**9):
        maxCandidate = 10**9
    if(minCandidate > 10**9):
        minCandidate = 10**9
    if(minCandidate < 1):
        minCandidate = 1
    currentMax = 0
    for i in range(minCandidate, maxCandidate + 1):
        amount = A * i + B * len(str(i))
        if(X > amount):
            currentMax = i
        elif (X == amount):
            print(i)
            return
        else:
            print(currentMax)
            return
    print(currentMax)
    return


INPUT = list(map(int, input().split()))
A = INPUT[0]
B = INPUT[1]
X = INPUT[2]
maxCandidate = 10**9
minCandidate = 0
if(A != 0):
    maxCandidate = math.ceil(X / A)
    minCandidate = math.floor((X - 9 * B) / A) - 1
else:
    minCandidate = X - 9 * B - 1

calcMaxNum(minCandidate, maxCandidate, A, B, X)
