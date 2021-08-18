class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort(reverse=True)

        def helper(goal, cnt):
            @lru_cache(None)
            def dp(i, tot, left):
                if tot == goal and left == 0:
                    return True
                if tot > goal or left == 0 or i == len(A):
                    return False
                return dp(i + 1, tot, left) or dp(i + 1, tot + A[i], left - 1)
            return dp(0, 0, cnt)
        tot = sum(A)
        for i in range(1, len(A) // 2 + 1):
            needed = tot * i / len(A)
            if int(needed) != needed:
                continue
            needed = int(needed)
            if helper(needed, i):
                print(needed)
                return True
        return False
