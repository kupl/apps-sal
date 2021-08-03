class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        minVal = 0
        maxVal = arr[0]
        for val in arr:
            if val < minVal:
                minVal = val
            if val > maxVal:
                maxVal = val
        low = minVal
        high = maxVal

        while(low < high):
            mid = high - (high - low) // 2

            if(self.mutationSum(mid, arr) <= target):
                low = mid
            else:
                high = mid - 1

        if (self.mutationSum(low, arr) == target):
            return low

        closestBelowInput = low
        closestBelowVal = self.mutationSum(closestBelowInput, arr)

        low = minVal
        high = maxVal
        while(low < high):
            mid = low + (high - low) // 2

            if(self.mutationSum(mid, arr) >= target):
                high = mid
            else:
                low = mid + 1
        if(self.mutationSum(high, arr) == target):
            return high

        closestAboveInput = high
        closestAboveVal = self.mutationSum(closestAboveInput, arr)

        if (target - closestBelowVal) <= (closestAboveVal - target):
            return closestBelowInput

        return closestAboveInput

    def mutationSum(self, m, arr):
        total = 0
        for val in arr:
            if(val > m):
                total += m
            else:
                total += val
        return total
