class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def helper(emp):
            if manager[emp]>=0:
                informTime[emp]+=helper(manager[emp])
                manager[emp]= -1
            return informTime[emp]
        return max(map(helper,manager))
