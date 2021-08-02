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
s = getIntList()
c = getIntList()
maxValue = 10**8 + 1
result = maxValue * 3
minLeft = [0] * n
minRight = [0] * n
minLeft[0] = c[0]
for i in range(1, n):
    minLeft[i] = min(c[i], minLeft[i - 1])
minRight[n - 1] = c[n - 1]
for i in range(n - 2, -1, -1):
    minRight[i] = min(c[i], minRight[i + 1])
minSLeft = [0] * n
maxSRight = [0] * n
minSLeft[0] = s[0]
for i in range(1, n):
    minSLeft[i] = min(s[i], minSLeft[i - 1])
maxSRight[n - 1] = s[n - 1]
for i in range(n - 2, -1, -1):
    maxSRight[i] = max(s[i], maxSRight[i + 1])
prices = [(c[j], j) for j in range(1, n - 1)]
prices.sort()
for currC, j in prices:
    if minLeft[j - 1] + c[j] + minRight[j + 1] >= result:
        continue
    if minSLeft[j - 1] >= s[j] or s[j] >= maxSRight[j + 1]:
        continue
    a = maxValue
    for i in range(j):
        if s[i] < s[j]:
            a = min(a, c[i])
    b = maxValue
    for k in range(j + 1, n):
        if (s[j] < s[k]):
            b = min(b, c[k])
    curr = a + b + c[j]
    result = min(result, curr)
if result == maxValue * 3:
    result = -1
print(result)
