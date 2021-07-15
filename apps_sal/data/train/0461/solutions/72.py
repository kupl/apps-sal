class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_list = collections.defaultdict(list)
        for i in range(len(manager)):
            manager_list[manager[i]].append(i)
        
        queue = [(headID, informTime[headID])]
        time = 0
        while queue:
            # print(queue)
            cur, cur_time = queue.pop(0)
            time = max(time, cur_time)
            if manager_list[cur] != []:
                print((cur, informTime[cur]))
                employees = manager_list[cur]
                manager_list[cur] = []
                for employee in employees:
                    queue.append((employee, cur_time + informTime[employee]))
        return time
        

