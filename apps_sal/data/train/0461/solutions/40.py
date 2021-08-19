class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_employee_dict = {}
        for i in range(n):
            m = manager[i]  # manager of i is n
            if m != -1:
                if m in manager_employee_dict:
                    manager_employee_dict[m].append(i)
                else:
                    manager_employee_dict[m] = [i]

        # want to start with the head node to get the max depth
        def chain_length(em):
            if em not in manager_employee_dict:
                return 0
            return informTime[em] + max(chain_length(em_n) for em_n in manager_employee_dict[em])
        if len(manager_employee_dict) == 0:
            return 0
        # num = max(chain_length(e) for e in manager_employee_dict)
        return chain_length(headID)
