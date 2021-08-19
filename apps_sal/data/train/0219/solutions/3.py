class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        score = 0
        dic = {}
        result = 0
        for (i, hour) in enumerate(hours):
            if hour > 8:
                score += 1
            else:
                score -= 1
            if score > 0:
                result = i + 1
            if score not in dic:
                dic[score] = i
            if score - 1 in dic:
                result = max(result, i - dic[score - 1])
        return result
