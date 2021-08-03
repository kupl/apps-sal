class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        states = collections.defaultdict(int)
        for a in arr:
            states[a] = states[a - difference] + 1
        return max(states.values())
