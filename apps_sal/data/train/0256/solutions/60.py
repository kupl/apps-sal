import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        ans = [0]
        high = max(piles)
        h = [H]

        def check(speed, piles):
            cost = 0
            for i in piles:
                cost += math.ceil(i / speed)
                if cost > h[0]:
                    return False
            return True

        def binary(low, high):
            if low > high:
                return high
            mid = (low + high) // 2
            if check(mid, piles):
                ans[0] = mid
                binary(low, mid - 1)
            else:
                binary(mid + 1, high)
        binary(low, high)
        return ans[-1]
