#!/bin/python
import sys
counter = 0
allstrs = []
def firstnum (inpu):
    out = ""
    for char in inpu:
        if char == ' ':
            break
        out += char
    return int(out)
def secondnum (inpu):
    first = True
    out = ""
    for char in inpu:
        if char == ' ' and not(first):
            break
        elif char == ' ' and first:
            first = False
        out += char
    return int(out)


for line in sys.stdin:
    if counter == 0:
        counter += 1
    else:
        allstrs.append(line)

removalfiles = []

removalfilesnums = list(map(int, allstrs[allstrs.__len__() - 1].split(" ")))
for i in range(0, removalfilesnums.__len__() - 0):
    removalfiles.append(allstrs[removalfilesnums[i] - 1])
removalfiles = [s.strip('\n') for s in removalfiles]

for ff in removalfiles:
    if removalfiles[0].__len__() != ff.__len__():
        print("No")
        return

outString = ""
for ii in range(0, removalfiles[0].__len__()):
    broke = False
    for ff in removalfiles:
        if ff[ii] != removalfiles[0][ii]:
            broke = True
            outString += '?'
            break
    if not broke:
        outString += removalfiles[0][ii]

checklist = [s.strip('\n') for s in [allstrs[i] for i in range(0, allstrs.__len__()) if i + 1 not in removalfilesnums]]
for line in checklist:
    test = False
    if line.__len__() == outString.__len__():
        test = True
        for charLine, charOut in zip(line, outString):
            if charLine != charOut and charOut != '?':
                test = False
    if test:
        print("No")
        return
print("Yes")
print(outString)

