from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        max_time_needed = 0
        children = defaultdict(list)
        for i, emp in enumerate(manager):
            children[emp].append(i)

        stack = [(headID, informTime[headID])]

        while stack:
            emp_id, time_taken = stack.pop()
            max_time_needed = max(max_time_needed, time_taken)

            for ch in children[emp_id]:
                stack.append((ch, time_taken + informTime[ch]))

        return max_time_needed
