class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # fix how many go into B and C
        # then we know what the goal is?
        # 4:1, B gets 4x as much as C
        # B gets 4/5, C gets 1/5
        # then knapsack on one of them (lower one)
        A.sort(reverse=True)

        def helper(goal, cnt):
            # knapsack
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
            # B gets i
            # C gets len(A)-i
            # B gets i/len(A) * tot
            needed = tot * i / len(A)
            if int(needed) != needed:
                continue
            needed = int(needed)
            if helper(needed, i):
                print(needed)
                return True
        return False
