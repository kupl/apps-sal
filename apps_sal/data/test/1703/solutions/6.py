import math


def getIntList():
    return list(map(int, input().split()))


def getTransIntList(n):
    first = getIntList()
    m = len(first)
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        result[i][0] = first[i]
    for j in range(1, n):
        curr = getIntList()
        for i in range(m):
            result[i][j] = curr[i]
    return result


n = int(input())
s = [''] * n
for i in range(n):
    s[i] = input()
leftTypes = dict()
rightTypes = dict()


def getLeftDepth(s):
    depth = 0
    for l in s:
        if l == '(':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return -1
    return depth


def getRightDepth(s):
    depth = 0
    for l in s[::-1]:
        if l == ')':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                return -1
    return depth


for currS in s:
    d = getLeftDepth(currS)
    if d >= 0:
        leftTypes[d] = leftTypes.get(d, 0) + 1
    if d <= 0:
        d = getRightDepth(currS)
        if d >= 0:
            rightTypes[d] = rightTypes.get(d, 0) + 1
result = 0
for d, l in leftTypes.items():
    result += l * rightTypes.get(d, 0)
print(result)
