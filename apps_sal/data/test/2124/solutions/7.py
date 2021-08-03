import re
import copy

t = int(input())

for i in range(t):
    n = int(input())
    senderList = []
    for x in input().split():
        senderList.append(x)

    m = int(input())
    msg = [None] * m
    resSenders = [None] * m
    possibleSenders = []
    for i in range(m):
        possibleSenders.append(copy.copy(senderList))

    for i in range(m):
        line = input()
        blocks = re.findall(r"[\w]+", line)

        for x in blocks:
            try:
                possibleSenders[i].remove(x)
            except:
                pass

        if line[0] != '?':
            resSenders[i] = blocks[0]
            if i > 0:
                try:
                    possibleSenders[i - 1].remove(resSenders[i])
                except:
                    pass
            if i + 1 < m:
                try:
                    possibleSenders[i + 1].remove(resSenders[i])
                except:
                    pass
        msg[i] = line[line.find(":") + 1:]

    resolved = False
    while True:
        done = True
        justPick = True
        for i in range(m):
            if resSenders[i] != None:
                continue
            if len(possibleSenders[i]) == 0:
                done = True
                resolved = True
                print("Impossible")
                break
            if len(possibleSenders[i]) == 1:
                resSenders[i] = possibleSenders[i][0]
                if i > 0:
                    try:
                        possibleSenders[i - 1].remove(resSenders[i])
                    except:
                        pass
                if i + 1 < m:
                    try:
                        possibleSenders[i + 1].remove(resSenders[i])
                    except:
                        pass
                justPick = False
            else:
                done = False
        if done:
            break
        if justPick:
            for i in range(m):
                if resSenders[i] == None:
                    resSenders[i] = possibleSenders[i][0]
                    if i + 1 < m:
                        try:
                            possibleSenders[i + 1].remove(resSenders[i])
                        except:
                            pass
            break

    if not resolved:
        for i in range(m):
            print(resSenders[i] + ":" + msg[i])
