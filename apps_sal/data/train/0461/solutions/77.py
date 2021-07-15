class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        if n == 1:
            return 0
        
        # need data structure to keep track of individual employees
        time = collections.defaultdict(int)
        
        # do some preprocessing
        # create a map worksUnder
        # id -> {ids of employees that work under this manager}
        worksUnder = collections.defaultdict(set)
        
        for i in range(n):
            # employee i works under manager[i]
            worksUnder[manager[i]].add(i)
        
        stack = [headID]
        while stack:
            managerID = stack.pop()
            for i in worksUnder[managerID]:
                    # employee i works under managerID
                    # emplyee i's time is his manager's time plus 
                    # his manager's inform time
                    time[i] = informTime[managerID] + time[managerID]
                    stack.append(i)
        
        return max(time.values())
