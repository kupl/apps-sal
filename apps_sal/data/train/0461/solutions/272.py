class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        company_dict = {}
        total_time = 0
        
        for i, m in enumerate(manager):
            if m not in company_dict:
                company_dict[m] = set([i])
            else:
                company_dict[m].add(i)
        
        def get_emp_inf_time(manager, time):
            nonlocal total_time
            if manager not in company_dict:
                total_time = max(total_time, time)
                return
            for e in company_dict[manager]:
                time_to_inform = time + informTime[manager]
                get_emp_inf_time(e, time_to_inform)
        
        head = list(company_dict[-1])[0]
        get_emp_inf_time(head, 0)
        return total_time
