from collections import deque


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        l = len(status)
        found = [False] * l

        run_q = deque([])
        wait_q = deque([])
        tmp_q = deque([])
        for box in initialBoxes:
            if status[box] == 1:
                run_q.append(box)
            else:
                wait_q.append(box)
        res = 0
        while run_q:
            box = run_q.popleft()

            res += candies[box]
            for key in keys[box]:
                status[key] = 1
            for found_box in containedBoxes[box]:
                wait_q.append(found_box)

            while wait_q:
                sleeping_box = wait_q.popleft()
                if status[sleeping_box] == 1:
                    run_q.append(sleeping_box)
                else:
                    tmp_q.append(sleeping_box)
            while tmp_q:
                wait_q.append(tmp_q.popleft())
        return res
