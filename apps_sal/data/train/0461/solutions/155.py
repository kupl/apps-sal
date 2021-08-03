class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        total_time = [0] * n
        total_time[headID] = informTime[headID]
        for i in range(n):
            if total_time[i] == 0:
                path = [i]
                c_id = manager[i]
                while c_id != -1 and total_time[c_id] == 0:
                    path.append(c_id)
                    c_id = manager[c_id]
                c_time = total_time[c_id]
                if len(path) > 0:
                    total_time[path[-1]] = informTime[path[-1]] + c_time
                    for j in range(len(path) - 2, -1, -1):
                        total_time[path[j]] = informTime[path[j]] + total_time[path[j + 1]]
        return max(total_time)
