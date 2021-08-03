class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        final = 0
        score = 0
        stack = {}
        for i in range(len(hours)):
            if hours[i] > 8:
                score += 1
            else:
                score -= 1
            stack.setdefault(score, i)
            if score > 0:
                final = i + 1
            if score - 1 in stack:
                final = max(final, i - stack[score - 1])
        return final
