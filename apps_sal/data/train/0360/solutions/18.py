class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def isvalid(mid):
            total = 0
            package = 1
            for weight in weights:
                if weight > mid:
                    return False
                total += weight
                if total > mid:
                    package += 1
                    total = weight
            return package <= D

        def binsearch(low, high):
            while low < high:
                mid = low + (high - low) // 2
                print(isvalid(mid), mid)
                if not isvalid(mid):
                    low = mid + 1
                else:
                    high = mid
            return low
        return binsearch(0, sum(weights))
