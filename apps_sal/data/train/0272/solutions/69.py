class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = collections.deque()
        n = len(status)

        for i in initialBoxes:
            q.append(i)
        key = set()
        res = 0
        while q:
            length = len(q)
            hasOpen = False
            for i in range(length):
                box = q.popleft()

                if status[box] == 0 and box not in key:
                    q.append(box)
                else:
                    hasOpen = True
                    res += candies[box]
                    for k in keys[box]:
                        key.add(k)
                    for x in containedBoxes[box]:
                        q.append(x)
            if not hasOpen:
                break
        return res
