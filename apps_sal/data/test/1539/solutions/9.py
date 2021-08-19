"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""
from sys import stdin, stdout


def main():
    n = int(stdin.readline())
    leg = [int(_) for _ in stdin.readline().split()]
    d = [int(_) for _ in stdin.readline().split()]
    pairedLD = []
    for (x, y) in zip(leg, d):
        pairedLD.append((x, y))
    pairedLD = sorted(pairedLD)
    legSet = set()
    suffixSum = dict()
    legFreq = dict()
    for (length, energy) in zip(leg, d):
        legSet.add(length)
        if length in suffixSum:
            suffixSum[length] += energy
            legFreq[length] += 1
        else:
            suffixSum[length] = energy
            legFreq[length] = 1
    legList = [x for x in legSet]
    legList = sorted(legList, reverse=True)
    total = 0
    for length in legList:
        suffixSum[length] += total
        total = suffixSum[length]
    ans = int(20000000.0)
    toRemove = 0
    available = 0
    removable = [0] * 201
    legList = sorted(legList)
    listLen = len(legList)
    idx = 0
    for i in range(listLen):
        curr = 0
        if i + 1 < listLen:
            curr += suffixSum[legList[i + 1]]
        toRemove = available - (legFreq[legList[i]] - 1)
        if toRemove < 0:
            toRemove = 0
        for j in range(1, 201):
            if removable[j] != 0 and removable[j] <= toRemove:
                curr += removable[j] * j
                toRemove -= removable[j]
            elif removable[j] > toRemove:
                curr += toRemove * j
                toRemove = 0
            if toRemove == 0:
                break
        available += legFreq[legList[i]]
        for j in range(legFreq[legList[i]]):
            removable[pairedLD[idx][1]] += 1
            idx += 1
        ans = min(ans, curr)
    print(ans)


def __starting_point():
    main()


__starting_point()
