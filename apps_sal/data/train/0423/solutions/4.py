class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = Counter()
        for v in arr:
            seen[v] = seen[v - difference] + 1
        return max(seen.values())
