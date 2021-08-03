class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub_h = {}
        for idx in range(n):
            if idx == headID:
                continue
            if manager[idx] not in sub_h:
                sub_h[manager[idx]] = [informTime[manager[idx]], idx]
            else:
                sub_h[manager[idx]].append(idx)
        self.res = 0

        def helper(cur, t):
            if cur not in sub_h:
                self.res = max(self.res, t)
                return
            for sub in sub_h[cur][1:]:
                helper(sub, t + sub_h[cur][0])

        helper(headID, 0)
        return self.res
