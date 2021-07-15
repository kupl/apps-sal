__author__ = 'ruckus'

def haveLast(Chains, Name):
    for i in range(len(Chains)):
        if Chains[i][len(Chains[i])-1] == Name:
            return i
    return -1

RepostNum = int(input())

Reposts = []

for i in range(RepostNum):
    Reposts.append(input().split())
    Reposts[i][0] = Reposts[i][0].upper()
    Reposts[i][2] = Reposts[i][2].upper()

MaxRepostLen = 1

Chains = []

for i in range(RepostNum):
    if Reposts[i][2] == 'Polycarp'.upper():
        Chains.append(['Polycarp'.upper(), Reposts[i][0]])
    else:
        num = haveLast(Chains, Reposts[i][2])
        if num >= 0:
            Chains[num].append(Reposts[i][0])
        else:
            for j in range(len(Chains)):
                if Reposts[i][2] in Chains[j]:
                    Chains.append(Chains[j][:Chains[j].index(Reposts[i][2])+1])
                    Chains[len(Chains)-1].append(Reposts[i][0])

for Chain in Chains:
    if len(Chain) > MaxRepostLen:
        MaxRepostLen = len(Chain)

print(MaxRepostLen)
