class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        maximum = 0
        cur = []
        closeddic = dict()
        size = 0
        for i in initialBoxes:
            if status[i] == 1:
                cur.append(i)
                size += 1
            else:
                closeddic[i] = 1
        consumed = dict()
        keysdic = dict()
        while size > 0:
            nex = []
            nsize = 0
            for i in cur:
                maximum += candies[i]
                consumed[i] = True
                for j in containedBoxes[i]:
                    if (status[j] == 1 or j in keysdic) and j not in consumed:
                        nex.append(j)
                        nsize += 1
                    elif status[j] == 0:
                        closeddic[j] = 1
                for j in keys[i]:
                    keysdic[j] = 1
                    if j in closeddic and j not in consumed:
                        del closeddic[j]
                        nex.append(j)
                        nsize += 1
            size = nsize
            cur = nex
        return maximum
