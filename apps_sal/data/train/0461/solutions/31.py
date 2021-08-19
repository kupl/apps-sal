class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        import heapq
        uninformed = set([i for i in range(n)])
        q = [(0, headID)]
        heapq.heapify(q)
        sub = collections.defaultdict(list)
        for i, v in enumerate(manager):
            sub[v].append(i)
        while q:
            # print(q)
            # print(uninformed)
            TI, ID = heapq.heappop(q)
            uninformed -= set([(ID)])
            if not uninformed:
                return TI
            for sb in sub[ID]:
                if sb in uninformed:
                    heapq.heappush(q, (TI + informTime[ID], sb))
        return -1
