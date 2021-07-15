class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        cnt = defaultdict(int)
        for i in arr:
            cnt[i] = cnt[i-d] + 1
        return max(cnt.values())
