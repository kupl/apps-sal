class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = {}
        for (i, man) in enumerate(manager):
            if man == -1:
                continue
            if man not in subs:
                subs[man] = set()
            subs[man].add(i)
        queue = [(headID, 0, 0)]
        informTimes = {}
        while queue:
            (curr, level, informedAt) = queue.pop()
            if curr not in subs:
                continue
            emps = subs[curr]
            for e in emps:
                if level not in informTimes:
                    informTimes[level] = -1
                currInformTime = informTime[curr] + informedAt
                informTimes[level] = max(informTimes[level], currInformTime)
                queue.append((e, level + 1, currInformTime))
        if not informTimes:
            return 0
        return max(informTimes.values())
