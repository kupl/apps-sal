class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinate = collections.defaultdict(list)
        for i in range(n):
            subordinate[manager[i]].append(i)

        def solve(ID):
            if subordinate[ID]:
                return max(solve(i) for i in subordinate[ID]) + informTime[ID]
            else:
                return 0
        return solve(headID)
