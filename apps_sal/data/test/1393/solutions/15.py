A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = A.swapcase()
Al = A + a
numS = [0 for i in Al]
numT = [0 for i in Al]
numT_ = [0 for i in Al]
s = input()
t = input()
t_ = t.swapcase()
yay = 0
whoops = 0
for i in range(len(Al)):
    numS[i] = s.count(Al[i])
    numT[i] = t.count(Al[i])
    numT_[i] += t_.count(Al[i])
    yay += min(numS[i], numT[i])
    if i <= 25:
        k = i + 26
    else:
        k = i - 26
    numT_[k] -= min(numS[i], numT[i])
    numS[i] -= min(numS[i], numT[i])
for i in range(len(Al)):
    whoops += min(numS[i], numT_[i])
print(yay, whoops)
