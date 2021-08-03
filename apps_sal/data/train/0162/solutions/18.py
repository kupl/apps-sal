class Solution:
    def longestCommonSubsequence(self, text1, text2):

        def compute(x, y):
            if x == len(text1):
                return 0
            if y == len(text2):
                return 0

            if text1[x] == text2[y]:
                return 1 + compute(x + 1, y + 1)

            return max([compute(x + 1, y), compute(x, y + 1)])

        cache = {}

        for x in range(-1, len(text1) + 1):
            cache[(x, -1)] = 0

        for y in range(-1, len(text2) + 1):
            cache[(-1, y)] = 0

        for x in range(len(text1)):
            for y in range(len(text2)):
                if text1[x] == text2[y]:
                    cache[(x, y)] = 1 + cache[(x - 1, y - 1)]
                else:
                    cache[(x, y)] = max([cache[(x, y - 1)], cache[(x - 1, y)]])

        return cache[(len(text1) - 1, len(text2) - 1)]
