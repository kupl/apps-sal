class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        seen = {}
        (result, score) = (0, 0)
        for (i, num) in enumerate(hours):
            score += 1 if num > 8 else -1
            if score > 0:
                result = i + 1
            elif score - 1 in seen:
                result = max(result, i - seen[score - 1])
            seen.setdefault(score, i)
        return result
