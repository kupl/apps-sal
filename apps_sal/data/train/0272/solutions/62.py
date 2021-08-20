class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = []
        res = 0
        vis = set()
        collected = set()
        for i in initialBoxes:
            q.append(i)
        while q:
            cur = q.pop(0)
            vis.add(cur)
            if status[cur] != 1 or cur in collected:
                continue
            res += candies[cur]
            collected.add(cur)
            for i in keys[cur]:
                status[i] = 1
                if i in vis:
                    q.append(i)
            for j in containedBoxes[cur]:
                q.append(j)
        return res
