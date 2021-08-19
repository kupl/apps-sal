class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        high = sum(weights)
        low = max(weights)

        def check(cap):
            cnt = 1
            summ = 0
            for w in weights:
                if summ + w <= cap:
                    summ += w
                else:
                    cnt += 1
                    summ = w
                if cnt > D:
                    return False
            return True
        while low != high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
