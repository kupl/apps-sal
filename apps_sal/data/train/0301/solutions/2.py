class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = defaultdict(list)
        for (i, n) in enumerate(B):
            memo[n].append(i)

        @lru_cache(None)
        def helper(index, taken):
            if index >= len(A):
                return 0
            count = 0
            if A[index] in memo:
                for i in memo[A[index]]:
                    if i > taken:
                        count = 1 + helper(index + 1, i)
                        break
            count = max(count, helper(index + 1, taken))
            return count
        return helper(0, -1)
