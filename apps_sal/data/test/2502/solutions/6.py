def getTableMP(Ss):
    lenS = len(Ss)
    table = [-1] * (lenS + 1)
    j = -1
    for i in range(lenS):
        while j >= 0 and Ss[i] != Ss[j]:
            j = table[j]
        j += 1
        table[i + 1] = j
    return table


Ss = input()
Ts = input()
(lenS, lenT) = (len(Ss), len(Ts))
num = (lenT + lenS - 1 + lenS - 1) // lenS
S2s = Ss * num
tableMP = getTableMP(Ts + '$' + S2s)
isFounds = [False] * lenS
for i in range(2 * lenT + 1, 2 * lenT + lenS + 1):
    if tableMP[i] >= lenT:
        isFounds[i - 2 * lenT - 1] = True
ans = 0
numDone = 0
for i in range(lenS):
    if not isFounds[i]:
        i = (i + lenT) % lenS
        for num in range(lenS + 1):
            if not isFounds[i]:
                ans = max(ans, num)
                numDone += num + 1
                break
            i = (i + lenT) % lenS
        else:
            ans = -1
            break
if numDone < lenS:
    ans = -1
print(ans)
