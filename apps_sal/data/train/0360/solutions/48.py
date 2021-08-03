class Solution:
    def trips(self, l, c):
        currSum = 0
        t, i = 0, 0
        n = len(l)
        while(i < n):
            if(currSum + l[i] > c):
                currSum = 0
                t = t + 1
            else:
                currSum = currSum + l[i]
                i = i + 1
        return t + 1

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low < high):
            mid = int(low + (high - low) / 2)
            if(self.trips(weights, mid) <= D):
                high = mid
            else:
                low = mid + 1
        return low
