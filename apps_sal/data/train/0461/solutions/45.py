from typing import List
from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_dict = defaultdict(list)
        for (index, curr_manager) in enumerate(manager):
            manager_dict[curr_manager].append(index)
        return self.dfs_num_of_minutes(headID, manager_dict, informTime)

    def dfs_num_of_minutes(self, curr_id, manager_dict, informTime):
        curr_inform_time = informTime[curr_id]
        direct_report_informa_time = 0
        for direct_report in manager_dict.get(curr_id, []):
            direct_report_informa_time = max(direct_report_informa_time, self.dfs_num_of_minutes(direct_report, manager_dict, informTime))
        return curr_inform_time + direct_report_informa_time
