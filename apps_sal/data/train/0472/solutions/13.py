from collections import deque


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = set()
        while queue:
            curr_index = queue.popleft()
            seen.add(curr_index)
            if arr[curr_index] == 0:
                return True
            if curr_index - arr[curr_index] >= 0 and curr_index - arr[curr_index] not in seen:
                queue.append(curr_index - arr[curr_index])
            if curr_index + arr[curr_index] < len(arr) and curr_index + arr[curr_index] not in seen:
                queue.append(curr_index + arr[curr_index])
        return False
