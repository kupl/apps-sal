class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        q = [[headID, informTime[headID]]]
        d = defaultdict(list)
        for i, val in enumerate(manager):
            d[val].append(i)
        res = 0
        while True:
            new_q = []
            cur_max_time = 0
            while q:
                index, time = q.pop()
                res = max(res, time)
                for v in d[index]:
                    new_q.append((v, time + informTime[v]))
            q = new_q[:]

            if not q:
                break
        return res
