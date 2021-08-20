class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        history = []
        count = 0
        limit = -1
        for i in light:
            history.append(light)
            limit = max(limit, i)
            if len(history) == limit:
                count += 1
        return count
