class Solution:

    class Node:

        def __init__(self, id):
            self.id = id
            self.next = []

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if len(manager) == 0:
            return 0
        directs = defaultdict(list)
        for (i, m) in enumerate(manager):
            directs[manager[i]].append(i)
        q = deque([(headID, 0)])
        t = 0
        while len(q) > 0:
            (curr, currT) = q.popleft()
            t = max(t, currT)
            if curr in directs:
                for d in directs[curr]:
                    q.append((d, currT + informTime[curr]))
        return t
