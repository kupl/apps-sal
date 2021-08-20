class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        def find(x, maps):
            if x in maps:
                maps[x] = find(maps[x], maps)
            else:
                return x
            return maps[x]

        def join(x, y, maps):
            (i, j) = (find(x, maps), find(y, maps))
            if i != j:
                if i < j:
                    maps[j] = i
                else:
                    maps[i] = j
        if not nums:
            return 0
        visited = {}
        maps = {}
        for i in nums:
            if i in visited:
                continue
            if i not in visited and i - 1 in visited:
                join(i - 1, i, maps)
            if i not in visited and i + 1 in visited:
                join(i + 1, i, maps)
            if i not in visited:
                visited[i] = 1
        if not maps:
            return 1
        for key in list(maps.keys()):
            join(maps[key], key, maps)
        d = Counter(list(maps.values()))
        return max(d.values()) + 1
