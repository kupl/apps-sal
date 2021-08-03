class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        total_time, company_dict = 0, {}
        for i, m in enumerate(manager):  # ix, emp
            if m not in company_dict:
                company_dict[m] = set([i])  # unique ix
            else:
                company_dict[m].add(i)  # in dict {ix:ID ...}

        def get_emp_inf_time(manager, time):
            nonlocal total_time
            if manager not in company_dict:  # new => {M:t ...}
                total_time = max(total_time, time)
                return
            for e in company_dict[manager]:
                time_to_inform = time + informTime[manager]  # [1] mng : emp with time
                get_emp_inf_time(e, time_to_inform)  # rec. [2] emp time
        head = list(company_dict[-1])[0]  # add the head
        get_emp_inf_time(head, 0)  # rec. [3]: add the last
        return total_time
