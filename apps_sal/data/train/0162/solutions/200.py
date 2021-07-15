class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1==len(text1) or p2==len(text2):
                return 0
            
            case1=memo_solve(p1+1, p2)
            first = text2.find(text1[p1], p2)
            case2=0
            if first != -1:
                case2 = 1 + memo_solve(p1+1, first +1)
            
            return max(case1, case2)
        return memo_solve(0, 0)

