class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_employee_dict = {}
        for i in range(n):
            m = manager[i]
            if m != -1:
                if m in manager_employee_dict:
                    manager_employee_dict[m].append(i)
                else:
                    manager_employee_dict[m] = [i]

        def chain_length(em):
            if em not in manager_employee_dict:
                return 0
            return informTime[em] + max(chain_length(em_n) for em_n in manager_employee_dict[em])
        if len(manager_employee_dict) == 0:
            return 0
        return chain_length(headID)
