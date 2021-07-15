import sys, os

def myreadline():

    #testFile = "461A-t"
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
#print(sm)
res = 0
res += sm*2
for x in l:
    sm -= x
    #print(sm)
    res += sm
res -= l[len(l)-1]

print(res)











