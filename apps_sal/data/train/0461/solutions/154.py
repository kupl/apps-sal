class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def func(parent, t):
            self.res = max(self.res, t)
            for child in subs[parent]:
                func(child, t + informTime[parent])

        subs = collections.defaultdict(set)
        for i, m in enumerate(manager):
            if m != -1:
                subs[m].add(i)
        self.res = 0
        func(headID, 0)
        return self.res
