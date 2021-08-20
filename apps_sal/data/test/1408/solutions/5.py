"""
Created on Jan 26, 2015

@author: mohamed265
"""
n = int(input())
tOne = [0]
tTwo = [0]
sizeOne = 1
sizetwo = 1
slon = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range(n):
    t = input().split()
    if t[0] == '1':
        tOne.append(int(t[1]))
        sizeOne += 1
    else:
        tTwo.append(int(t[1]))
        sizetwo += 1
tOne.sort(reverse=False)
tTwo.sort(reverse=False)
for i in range(1, sizeOne):
    tOne[i] += tOne[i - 1]
for i in range(1, sizetwo):
    tTwo[i] += tTwo[i - 1]
tOne.reverse()
tTwo.reverse()
for i in range(sizeOne):
    for j in range(sizetwo):
        if i + 2 * j >= tOne[i] + tTwo[j]:
            slon = min(slon, i + 2 * j)
print(slon)
