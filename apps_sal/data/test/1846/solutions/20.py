f = open('input.txt', 'r')
fContent = f.readlines()
f.close()
n = int(fContent[0])
temperatures = list(map(int, fContent[1].split()))
zeros = 0
pos = 0
neg = 0
for x in temperatures:
    if x < 0:
        neg += 1
    elif x > 0:
        pos += 1
    else:
        zeros += 1
changes = 99999999999
leftPos = 0
leftNeg = 0
for i in range(len(temperatures) - 1):
    if temperatures[i] < 0:
        leftNeg += 1
    elif temperatures[i] > 0:
        leftPos += 1
    changes = min(changes, leftPos + zeros + (neg - leftNeg))
outF = open('output.txt', 'w+')
outF.write(str(changes))
outF.close()
