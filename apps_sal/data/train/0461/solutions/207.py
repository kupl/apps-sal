class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        sub = collections.defaultdict(list)
        for i in range(len(manager)):
            sub[manager[i]].append(i)

        total = 0
        q = collections.deque([(headID, 0)])
        while q:
            employee, time = q.popleft()
            if not sub[employee]:
                total = max(total, time)
            for nxt in sub[employee]:
                q.append((nxt, time + informTime[employee]))
        return total
