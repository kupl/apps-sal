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
                    informTimes[level] = []
                currInformTime = informTime[curr] + informedAt
                informTimes[level].append(currInformTime)
                queue.append((e, level + 1, currInformTime))
        if not informTimes:
            return 0
        maxInformTime = -1
        for (level, informTimesLevel) in list(informTimes.items()):
            maxInformTime = max(maxInformTime, max(informTimesLevel))
        return maxInformTime
