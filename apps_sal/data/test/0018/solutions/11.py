#! /bin/python

s = input()
resultBase = ""
resultRest = ""
best = len(s) - 1
mini = [0] * len(s)

for i in range(len(s) - 1, -1, -1):
    mini[i] = best
    if s[best] >= s[i]:
        best = i

for i in range(len(s)):
    resultRest += s[i]
    while len(resultRest) > 0 and resultRest[-1] <= s[mini[i]]:
        resultBase += resultRest[-1]
        resultRest = resultRest[:-1]
    
print(resultBase + resultRest[::-1])

