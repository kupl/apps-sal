def inform(head, subs, informTime) -> int:
    subordinates = subs[head]
    if not subordinates:
        return 0
    return informTime[head] + max(inform(sub, subs, informTime) for sub in subordinates)


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = [[] for _ in range(n)]
        for sub, man in enumerate(manager):
            if man >= 0:
                subs[man].append(sub)
        return inform(headID, subs, informTime)
