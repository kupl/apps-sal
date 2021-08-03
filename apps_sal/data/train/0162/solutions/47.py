class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #         h = {}
        #         def longest(t1, t2):
        #             if (t1, t2) in h:
        #                 return h[(t1, t2)]
        #             if not t1 or not t2:
        #                 h[(t1, t2)] = 0
        #                 return h[(t1, t2)]
        #             elif t1[0] == t2[0]:
        #                 h[(t1, t2)] = 1 + longest(t1[1:], t2[1:])
        #                 return h[(t1, t2)]
        #             else:
        #                 h[(t1, t2)] = max(longest(t1, t2[1:]), longest(t1[1:], t2))
        #                 return h[(t1, t2)]

        #         return longest(text1, text2)

        @lru_cache(None)
        def longest(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + longest(i + 1, j + 1)
            else:
                return max(longest(i, j + 1), longest(i + 1, j))

        return longest(0, 0)
