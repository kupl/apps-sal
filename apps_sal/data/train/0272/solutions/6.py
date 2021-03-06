class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        reachable = [False] * len(status)
        visited = [False] * len(status)
        for box in initialBoxes:
            reachable[box] = True
            visited[box] = True
        for i in range(len(containedBoxes)):
            for inside in containedBoxes[i]:
                reachable[inside] = False
        queue = initialBoxes
        target = []
        ret = 0
        while queue:
            cnt = 0
            for box in queue:
                if status[box] == 1 and reachable[box]:
                    cnt += 1
                    ret += candies[box]
                    visited[box] = True
                    for key in keys[box]:
                        if status[key] == 0:
                            status[key] = 1
                            if reachable[key] and (not visited[key]):
                                target.append(key)
                                visited[key] = True
                    for inside in containedBoxes[box]:
                        reachable[inside] = True
                        if status[inside] == 1 and (not visited[inside]):
                            target.append(inside)
                            visited[inside] = True
                else:
                    target.append(box)
            if cnt == 0:
                break
            queue = target
            target = []
        return ret
