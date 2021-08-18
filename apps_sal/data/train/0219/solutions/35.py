class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score, longest = 0, 0
        index = {}
        for i, n in enumerate(hours):
            score += 1 if n > 8 else -1
            if score > 0:
                longest = max(longest, i + 1)
            index.setdefault(score, i)
            if score - 1 in index:
                longest = max(longest, i - index[score - 1])
        return longest
