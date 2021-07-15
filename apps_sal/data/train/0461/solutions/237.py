class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hmap = {}
        for i, m in enumerate(manager):
            hmap[m] = hmap.get(m, []) + [i]
        
        stack = [(headID, 0)]
        res = 0
        
        while stack:
            m, val = stack.pop()
            res = max(res, val)
            if m not in hmap:
                continue
            val += informTime[m]
            for e in hmap[m]:
                stack.append((e, val))
        
        return res
