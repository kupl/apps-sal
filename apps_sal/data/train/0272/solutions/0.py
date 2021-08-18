class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        reachable = [False] * len(status)
        visited = [False] * len(status)
        for box in initialBoxes:
            reachable[box] = True
        for i in range(len(containedBoxes)):
            for inside in containedBoxes[i]:
                reachable[inside] = False
        queue = initialBoxes
        target = []
        ret = 0
        while queue:
            for box in queue:
                if status[box] == 1 and reachable[box] and not visited[box]:
                    ret += candies[box]
                    visited[box] = True
                    for key in keys[box]:
                        if status[key] == 0:
                            status[key] = 1
                            if reachable[key]:
                                target.append(key)
                    for inside in containedBoxes[box]:
                        reachable[inside] = True
                        if status[inside] == 1:
                            target.append(inside)
                else:
                    target.append(box)
            if target == queue:
                break
            queue = target
            target = []
        return ret
