class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        N = len(status)
        queue = list()
        unopened = set()
        for i in initialBoxes:
            if status[i] == 1:
                queue.append(i)
            else:
                unopened.add(i)

        candiesCount = 0

        while len(queue) > 0:
            top = queue.pop(0)
            candiesCount += candies[top]

            for k in keys[top]:
                status[k] = 1
                if {k}.issubset(unopened):
                    queue.append(k)
                    unopened.remove(k)
            for c in containedBoxes[top]:
                if status[c] == 1:
                    queue.append(c)
                else:
                    unopened.add(c)
        return candiesCount
