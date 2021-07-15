from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        ownedkeys = set()
        allkz = set()
        for k in keys:
            for l in k:
                allkz.add(l)
        # for i, b in enumerate(status):
            # if not b and b not in allkz:
                # unreachable.add(b)
            
        opened = set(i for i, b in enumerate(status) if not b and i not in allkz) # treat unreachable as already opened
        res = 0
        while q:
            curBox = q.popleft()
            if curBox not in opened:
                if status[curBox] or curBox in ownedkeys:
                    opened.add(curBox)
                    for k in keys[curBox]:
                        ownedkeys.add(k)
                    res += candies[curBox]
                    q += containedBoxes[curBox]
                else:
                    q.append(curBox)
        return res           
                
                

