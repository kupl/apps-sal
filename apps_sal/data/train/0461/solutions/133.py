class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        stack = [(headID, 0)]

        ans = 0
        dic = {}
        for e, m in enumerate(manager):
            dic[m] = dic.get(m, set())
            dic[m].add(e)
        while stack:
            em, time = stack.pop(0)
            if informTime[em] == 0:
                ans = max(ans, time)
            else:
                for e in dic.get(em, []):
                    stack.append((e, informTime[em] + time))
        return ans
