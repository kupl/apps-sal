class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)

        def count(c: int) -> int:
            ans = 1
            curr = weights[0]
            for i in range(1, n):
                if curr + weights[i] > c:
                    ans += 1
                    curr = weights[i]
                else:
                    curr += weights[i]
            return ans
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            if count(m) > D:
                l = m + 1
            else:
                r = m
        return l
