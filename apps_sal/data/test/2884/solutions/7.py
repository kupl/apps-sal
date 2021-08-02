class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [None] + [set() for i in range(target)]
        candidates.sort()
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                dp[i + j] |= {_ + (i,) for _ in dp[j]}
            dp[i].add((i,))
        return list(dp[-1])
