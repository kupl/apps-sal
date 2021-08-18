import math

n, m = list(map(int, input().split()))
SYMBOLS = ['&', '*', '

strs = []

for i in range(n):
    strs.append(list(input()))

minA = [m] * n
minD = [m] * n
minS = [m] * n
for i, s in enumerate(strs):
    for j, c in enumerate(list(s)):
        dist = min(j, m - j)
        if c.isalpha() and minA[i] > dist:
            minA[i] = dist
        if c.isdigit() and minD[i] > dist:
            minD[i] = dist
        if c in SYMBOLS and minS[i] > dist:
            minS[i] = dist

minDist = math.inf
for i in range(n):
    for j in range(n):
        for k in range(n):
            summa = minA[i] + minD[j] + minS[k]
            if i != j and j != k and i != k and minDist > summa:
                minDist = summa

print(minDist)
