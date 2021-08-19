class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if D == 1:
            return sum(weights)
        start = max(max(weights), -(-sum(weights) // D))
        end = sum(weights)
        n = len(weights)

        def validate(x):
            count = 0
            i = 0
            while count < D:
                cur = 0
                while i < n and cur <= x:
                    cur += weights[i]
                    i += 1
                i -= 1
                count += 1
            if i == n - 1 and cur <= x:
                return True
            return False
        while start < end:
            m = (start + end) // 2
            if validate(m):
                end = m
            else:
                start = m + 1
        return start
