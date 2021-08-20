class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        weights = [1,2,3,4,5,6,7,8,9,10], D = 5

        left = 10
        right = 15
        mid = 15
        """
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            count = 1
            bucket = 0
            for w in weights:
                if bucket + w <= mid:
                    bucket += w
                else:
                    bucket = w
                    count += 1
            if count <= D:
                right = mid
            else:
                left = mid + 1
        return left
