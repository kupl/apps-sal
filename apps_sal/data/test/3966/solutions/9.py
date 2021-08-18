import sys
import os


def myreadline():

    testFile = ""

    if testFile:
        if not hasattr(myreadline, "fTest"):
            myreadline.fTest = open(os.path.join(os.path.dirname(__file__), testFile))
        return myreadline.fTest.readline()
    else:
        return input()


def myreadlineint():
    return [int(x) for x in myreadline().split()]


n, = myreadlineint()
l = myreadlineint()
l.sort()

sm = sum(l)
res = 0
res += sm * 2
for x in l:
    sm -= x
    res += sm
res -= l[len(l) - 1]

print(res)
