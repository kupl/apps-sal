class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left + 1 < right:
            mid = left + (right - left) // 2
            print(mid)
            curr = 0
            res = 1
            for w in weights:
                if curr + w > mid:
                    res += 1
                    curr = w
                else:
                    curr += w
            if res > D:  # !!here use >, since mid is impossible to meet the requireent
                left = mid
            else:  # !!here means <=, since there might be smaller mid
                right = mid

        res = 1
        curr = 0
        for w in weights:
            if curr + w > left:
                res += 1
                curr = w
            else:
                curr += w
        if res <= D:
            return left
        return right
