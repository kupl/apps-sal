class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        haskeys = status[:]
        seen = [0] * len(status)
        q = collections.deque()

        for box in initialBoxes:
            seen[box] = 1
            if(haskeys[box]):
                q.append(box)

        res = 0
        while q:

            boxi = q.popleft()
            res += candies[boxi]

            for nei in containedBoxes[boxi]:
                seen[nei] = 1
                if(haskeys[nei]):
                    q.append(nei)

            for key in keys[boxi]:
                if(seen[key] and haskeys[key] == 0):
                    q.append(key)
                haskeys[key] = 1

        return res
