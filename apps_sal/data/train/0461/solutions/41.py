class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        for (idx, man) in enumerate(manager):
            subordinates[man].append(idx)
        from collections import deque
        queue = deque()
        queue.append((headID, 0))
        ans = 0
        while queue:
            (node, time) = queue.popleft()
            ans = max(ans, time)
            for sub in subordinates[node]:
                queue.append((sub, time + informTime[node]))
        return ans
