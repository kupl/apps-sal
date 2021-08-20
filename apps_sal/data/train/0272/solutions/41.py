class Solution:

    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        access = [0] * n
        source = []
        visited = set()
        for i in initialBoxes:
            access[i] = 1
            visited.add(i)
            source.append(i)
        ans = 0
        while source:
            i = source.pop()
            ans += candies[i]
            for j in containedBoxes[i]:
                access[j] = 1
            for j in keys[i]:
                status[j] = 1
            for j in containedBoxes[i]:
                if j not in visited and status[j]:
                    visited.add(j)
                    source.append(j)
            for j in keys[i]:
                if j not in visited and access[j]:
                    visited.add(j)
                    source.append(j)
        return ans
