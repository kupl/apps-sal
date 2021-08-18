import sys


def input():
    return sys.stdin.readline()[:-1]


def getInt():
    return int(input())


def getIntIter():
    return list(map(int, input().split()))


def getIntList():
    return list(getIntIter())


for _ in range(getInt()):
    n = getInt()
    nums = getIntList()
    minSum = 0
    currSum = 0
    for num in nums:
        currSum += num
        minSum = min(currSum, minSum)
    print(abs(minSum))
