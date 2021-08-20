class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        timeNeed = [-1] * n

        def get_info_time(m):
            if timeNeed[m] != -1:
                return timeNeed[m]
            m_dad = manager[m]
            if m_dad == -1:
                timeNeed[m] = 0
            else:
                timeNeed[m] = get_info_time(m_dad) + informTime[m_dad]
            return timeNeed[m]
        for i in range(n):
            get_info_time(i)
        return max(timeNeed)
