class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def find_ttk(e):
            if ttk[e] == -1:
                m = manager[e]
                if m == -1:
                    ttk[e] = 0
                else:
                    ttk[e] = find_ttk(m) + informTime[m]
            return ttk[e]
        ttk = [-1] * n
        for e in range(n):
            if ttk[e] == -1:
                ttk[e] = find_ttk(e)
        return max(ttk)
