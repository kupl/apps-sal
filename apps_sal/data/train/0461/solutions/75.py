class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def check(manager, informTime, total_time, cur):
            if total_time[cur] >= 0:
                return total_time[cur]
            if manager[cur] == -1:
                total_time[cur] = 0
                return 0
            boss = manager[cur]
            total_time[cur] = check(manager, informTime, total_time, boss) + informTime[boss]
            return total_time[cur]

        total_time = [-1] * n
        rtv = 0
        for i in range(n):
            rtv = max(rtv, check(manager, informTime, total_time, i))
        return rtv
