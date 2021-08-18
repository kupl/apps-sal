class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.dfs1(rating, []) + self.dfs2(rating, [])

    def dfs1(self, array, path):
        if len(path) == 3:
            return 1
        val = 0
        for i in range(len(array)):
            if not path or path[-1] > array[i]:
                val += self.dfs1(array[i + 1:], path + [array[i]])
        return val

    def dfs2(self, array, path):
        if len(path) == 3:
            return 1
        val = 0
        for i in range(len(array)):
            if not path or path[-1] < array[i]:
                val += self.dfs2(array[i + 1:], path + [array[i]])
        return val
