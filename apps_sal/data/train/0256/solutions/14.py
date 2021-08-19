class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # want to search for K - this is the variable to change

        # if piles in sorted order - based on length of pile and hours - need to get average eats in the pile

        # let K = 1 to max(piles)

        # per hour - go through the piles and eat K bananas before time limit is up
        # O(N) time to go through all piles N
        # K is split via binary search log(K)

        # log(K) * N times

        low = 1
        high = max(piles)

        # the piles is not the one we want to find - its K

        # take too much time to eat - raise K
        # too little time to eat - lower K
        # set timer
        # always a solution
        def possible(k):
            time = 0
            # find out how much time it takes
            for pile in piles:
                time += (pile - 1) // k + 1
            return time <= H

        while low <= high:
            mid = low + (high - low) // 2
            outcome = possible(mid)

            # check if its possible
            if possible(mid):  # just right
                high = mid - 1
            else:
                low = mid + 1

        return low  # should not hit - always solution
