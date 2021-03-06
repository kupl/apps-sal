class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def func(parent, t):
            tt = t + informTime[parent]
            self.res = max(self.res, tt)
            for child in subs[parent]:
                func(child, tt)
        subs = collections.defaultdict(set)
        for (i, m) in enumerate(manager):
            if m != -1:
                subs[m].add(i)
        self.res = 0
        func(headID, 0)
        return self.res
