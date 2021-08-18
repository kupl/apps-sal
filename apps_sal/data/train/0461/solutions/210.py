class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = collections.deque([(headID, 0)])
        subordinates = collections.defaultdict(list)

        for subordinate, supervisor in enumerate(manager):
            subordinates[supervisor].append(subordinate)

        time = 0

        while queue:
            supervisor, currentInformTime = queue.popleft()
            time = max(time, currentInformTime)

            for subordinate in subordinates[supervisor]:
                queue.append((subordinate, currentInformTime + informTime[supervisor]))

        return time
