class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        retval = sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            (temp, count) = (0, 1)
            for i in range(len(weights)):
                temp += weights[i]
                if temp > mid:
                    temp = weights[i]
                    count += 1
                elif temp == mid:
                    temp = 0
                    count += 1
            if count > D:
                left = mid + 1
            else:
                retval = mid
                right = mid - 1
        return retval
