from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            n = len(text1)
            m = len(text2)
            if n == p1 or m == p2:
                return 0

            # case1 = memo_solve(p1+1,p2)
            # index = text2.find(text1[p1],p2)
            # if index !=-1:
            #     case2 = 1+memo_solve(p1+1,index+1)
            # else:
            #     case2 = 0

            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            return max(memo_solve(p1 + 1, p2), memo_solve(p1, p2 + 1))
        return memo_solve(0, 0)
