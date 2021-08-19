class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # use binary search to find the correct value
        maxPile = 0
        for i in piles:
            if i > maxPile:
                maxPile = i

        low = 1
        high = maxPile

        minVal = maxPile
        while low <= high:
            middle = (low + high) // 2
            numHours = 0
            for j in piles:
                numHours += j // middle
                if j % middle > 0:
                    numHours += 1

            if numHours <= H:
                minVal = middle
                high = middle - 1
            else:
                low = middle + 1

        return minVal
