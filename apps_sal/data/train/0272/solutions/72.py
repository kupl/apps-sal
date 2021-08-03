class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        maxCandy = 0
        keyset = set()
        numbox = len(status)
        q = list(initialBoxes)
        unopenedBOXES = []
        while q:
            for _ in range(len(q)):
                thisbox = q.pop(0)
                if status[thisbox] == 1 or thisbox in keyset:
                    maxCandy += candies[thisbox]
                    candies[thisbox] = 0
                    for key in keys[thisbox]:
                        keyset.add(key)
                else:
                    unopenedBOXES.append(thisbox)
                for x in containedBoxes[thisbox]:
                    q.append(x)

        for unopenedBOX in unopenedBOXES:
            if unopenedBOX in keyset:
                maxCandy += candies[unopenedBOX]

        return maxCandy
