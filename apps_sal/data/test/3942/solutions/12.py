'''

@author: linhz
'''

import sys


def __starting_point():
    s = input()
    leftCount = 0
    ansList = []
    ansFlag = True
    sharpCount = 0
    for c in s:
        if c == '(':
            leftCount += 1
        elif c == ')':
            leftCount -= 1
            if leftCount < 0:
                ansFlag = False
        elif c == '#':
            leftCount -= 1
            if leftCount < 0:
                ansFlag = False
            else:
                ansList.append(1)
                sharpCount += 1
        else:
            sys.stderr.write("Unexpected character:%c" % (c))
    if ansFlag:
        ansList[-1] += leftCount
        leftCount = 0
        sharpCount = 0
        for c in s:
            if c == '(':
                leftCount += 1
            elif c == ')':
                leftCount -= 1
                if leftCount < 0:
                    ansFlag = False
            elif c == '#':
                leftCount -= ansList[sharpCount]
                sharpCount += 1
                if leftCount < 0:
                    ansFlag = False
            else:
                sys.stderr.write("Unexpected character:%c" % (c))
        if ansFlag:
            for i in ansList:
                print(i)
        else:
            print(-1)
    else:
        print(-1)


__starting_point()
