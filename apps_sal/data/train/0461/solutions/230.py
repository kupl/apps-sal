from collections import deque


class Solution:

    def max_at_level(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = deque([headID])
        final_time_list = []
        while len(subs) > 0:
            managers_at_level = len(subs)
            level_time_list = []
            for i in range(managers_at_level):
                current_sub = subs.popleft()
                level_time_list.append(informTime[current_sub])
                subs += [index for index, val in enumerate(manager) if val == current_sub]
            final_time_list.append(level_time_list)

        total_time = 0
        for level_list in final_time_list:
            total_time += max(level_list)
        return total_time

    def numOfMinutesRecu(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = [index for index, val in enumerate(manager) if val == headID]
        if subs:
            time_sum = []
            for sub in subs:
                time_sum.append(self.numOfMinutes(n, sub, manager, informTime) + informTime[headID])
            return max(time_sum)
        else:
            return informTime[headID]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        stack = [(headID, informTime[headID])]
        res = 0

        children = defaultdict(list)
        for i, e in enumerate(manager):
            children[e].append(i)

        while stack:
            curr_id, curr_time = stack.pop()
            res = max(res, curr_time)
            #children = [index for index, val in enumerate(manager) if val == curr_id]
            for child in children[curr_id]:
                stack.append((child, curr_time + informTime[child]))
        return res
