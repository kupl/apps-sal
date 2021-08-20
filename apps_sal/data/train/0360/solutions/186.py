class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        n = len(weights)
        while lo < hi:
            guess = lo + (hi - lo) // 2
            guessDays = 1
            currLoad = 0
            for i in range(n):
                if currLoad + weights[i] > guess:
                    currLoad = 0
                    guessDays += 1
                currLoad += weights[i]
            if guessDays <= D:
                hi = guess
            else:
                lo = guess + 1
        return lo
