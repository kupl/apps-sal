class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2

            hours = 0
            s = i = 0
            rem = 0
            while i < len(piles):
                hours += int(math.ceil(piles[i] / mid))
                i += 1
            # print(mid, hours)
            if hours <= H:
                right = mid
            else:
                left = mid + 1
        return left
