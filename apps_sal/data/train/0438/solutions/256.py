def getGroup(groupsByNum, n):
    path = []
    while groupsByNum[n] != n:
        path.append(n)
        n = groupsByNum[n]
    for x in path:
        groupsByNum[x] = n
    return n


def joinGroups(a, b, groupsByNum, sizeByGroup, groupBySize):
    try:
        b = getGroup(groupsByNum, b)
        a = getGroup(groupsByNum, a)
        if a != b:
            aSize = sizeByGroup[a]
            bSize = sizeByGroup[b]
            if aSize > bSize:
                (a, b) = (b, a)
                (aSize, bSize) = (bSize, aSize)
            groupsByNum[a] = b
            del sizeByGroup[a]
            sizeByGroup[b] += aSize
            groupBySize[aSize].remove(a)
            groupBySize[bSize].remove(b)
            try:
                groupBySize[sizeByGroup[b]].add(b)
            except KeyError:
                groupBySize[sizeByGroup[b]] = {b}
            return True
        else:
            return False
    except KeyError:
        return False


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        sizeByGroup = dict()
        groupBySize = {1: set()}
        groupsByNum = dict()
        result = -1
        for (step, x) in enumerate(arr, 1):
            groupsByNum[x] = x
            groupBySize[1].add(x)
            sizeByGroup[x] = 1
            joinGroups(x, x + 1, groupsByNum, sizeByGroup, groupBySize)
            joinGroups(x, x - 1, groupsByNum, sizeByGroup, groupBySize)
            try:
                if len(groupBySize[m]) > 0:
                    result = step
            except KeyError:
                pass
        return result
