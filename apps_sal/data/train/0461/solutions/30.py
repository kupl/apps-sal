class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time = [-1] * n
        time[headID] = 0
        result = 0

        for i in range(n):
            if time[i] == -1:
                index = i
                path = []

                while time[index] == -1:
                    path.append(index)
                    index = manager[index]

                for j in reversed(path):
                    time[j] = time[manager[j]] + informTime[manager[j]]
                    result = max(result, time[i])

        return result
