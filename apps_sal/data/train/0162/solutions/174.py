class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lookup = [[None for x in range(len(text2))] for y in range(len(text1))]

        def helper(s1, s2, pos1, pos2):
            nonlocal lookup
            if pos1 >= len(s1):
                return 0
            elif pos2 >= len(s2):
                return 0
            elif lookup[pos1][pos2] is not None:
                return lookup[pos1][pos2]
            else:
                if s1[pos1] == s2[pos2]:
                    lookup[pos1][pos2] = max(1 + helper(s1, s2, pos1 + 1, pos2 + 1),
                                             helper(s1, s2, pos1 + 1, pos2 + 1),
                                             helper(s1, s2, pos1, pos2 + 1),
                                             helper(s1, s2, pos1 + 1, pos2))
                    return lookup[pos1][pos2]
                else:
                    lookup[pos1][pos2] = max(helper(s1, s2, pos1 + 1, pos2 + 1),
                                             helper(s1, s2, pos1, pos2 + 1),
                                             helper(s1, s2, pos1 + 1, pos2))
                    return lookup[pos1][pos2]
        return helper(text1, text2, 0, 0)
