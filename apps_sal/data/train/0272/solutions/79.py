class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        keyHold = set([idx for idx, b in enumerate(status) if b == 1])
        boxHold = set(initialBoxes)
        opened = set()
        while True:
            flag = False
            newKey = set()
            newBox = set()
            for b in boxHold:
                if b in keyHold:
                    opened.add(b)
                    flag = True
                    for k in keys[b]:
                        newKey.add(k)
                    for nb in containedBoxes[b]:
                        if nb not in opened:
                            newBox.add(nb)
            if not flag:
                break
            for k in newKey:
                keyHold.add(k)
            for b in newBox:
                boxHold.add(b)
            for b in opened:
                boxHold.discard(b)
        return sum([c for idx, c in enumerate(candies) if idx in opened])

