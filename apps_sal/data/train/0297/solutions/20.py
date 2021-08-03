class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = {}

        for i in tiles:
            if i not in count:
                count[i] = 0
            count[i] += 1

        op = set()
        for ch in count:
            tempString = ch
            op.add(tempString)
            count[ch] -= 1
            tempCount = count.copy()
            buildString(tempString, tempCount, op)
            count[ch] += 1

        return len(op)


def buildString(currString, count, op):
    flag = True
    for i in count:
        if count[i] != 0:
            flag = False
            break
    if flag:
        return

    for ch in count:
        if count[ch] == 0:
            continue
        tempString = currString
        tempString += ch

        op.add(tempString)
        count[ch] -= 1

        tempCount = count.copy()
        buildString(tempString, tempCount, op)
        count[ch] += 1
