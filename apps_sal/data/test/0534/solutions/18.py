tstring = str(input())
queuelist = list(input())
finalqueue = ''

t = int(tstring[tstring.index(' ') + 1:])

for j in range(0, t):
    for i in range(0, len(queuelist) - 1):
        if queuelist[i] == 'B' and queuelist[i + 1] == 'G':
            queuelist[i] = 'G'
            queuelist[i + 1] = 'X'
    for i in range(0, len(queuelist)):
        if queuelist[i] == 'X':
            queuelist[i] = 'B'

for i in range(0, len(queuelist)):
    finalqueue += queuelist[i]

print(finalqueue)
