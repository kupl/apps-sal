class Solution:

    def findLongestPath(self, tree, root, informTime):
        return max([self.findLongestPath(tree, child, informTime) for child in tree[root]] + [0]) + informTime[root]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mapM2E = collections.defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            else:
                mapM2E[manager[i]].append(i)
        return self.findLongestPath(mapM2E, headID, informTime)
