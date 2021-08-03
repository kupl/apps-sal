class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        for em, ma in enumerate(manager):
            dic[ma].append(em)

        queue = deque([(headID, 0)])
        res = 0
        while queue:
            for _ in range(len(queue)):
                ma, needed_time = queue.popleft()
                res = max(res, needed_time)
                for sub in dic[ma]:
                    queue.append((sub, needed_time + informTime[ma]))
        return res
