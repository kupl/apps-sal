class Solution:
    def get_managers_delay(self, index: int, cache: List[int], manager: List[int], informTime: List[int]) -> int:
        if manager[index] == -1:
            return informTime[index]

        if cache[index] != -1:
            return cache[index]

        managers_delay = self.get_managers_delay(manager[index], cache, manager, informTime)
        cache[index] = managers_delay + informTime[index]

        return cache[index]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        cache = [-1] * n
        max_inform_time = 0

        for i in range(n):
            inform_time = self.get_managers_delay(i, cache, manager, informTime)
            max_inform_time = max(max_inform_time, inform_time)

        return max_inform_time
