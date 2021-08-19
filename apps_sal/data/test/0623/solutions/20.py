__author__ = 'sandeepmellacheruvu'
(x, y) = map(int, input().split())
numMins = 0
prevElse = None
while True:
    if x > y:
        if prevElse == False:
            if x == 2:
                numMins += 1
            break
        prevElse = False
        while x - 2 > 0:
            x = x - 2
            y = y + 1
            numMins += 1
    else:
        if prevElse == True:
            if y == 2:
                numMins += 1
            break
        prevElse = True
        while y - 2 > 0:
            x = x + 1
            y = y - 2
            numMins += 1
print(numMins)
