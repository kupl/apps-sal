class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = Counter()
        for a in arr:
            memo[a] = memo[a - difference] + 1
        return max(memo.values())
