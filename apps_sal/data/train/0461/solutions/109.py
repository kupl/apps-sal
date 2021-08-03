class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        time = [-1] * n
        time[headID] = 0
        result = 0

        for i in range(n):
            # if the index isn't visited (hasn't already been found with index=manager[index])
            if time[i] == -1:
                # search down a path
                index = i
                path = []

                # follows path of manager to subordinate
                while time[index] == -1:
                    path.append(index)
                    index = manager[index]

                # adds everything together
                for j in reversed(path):
                    time[j] = time[manager[j]] + informTime[manager[j]]
                    result = max(result, time[i])

        return result
