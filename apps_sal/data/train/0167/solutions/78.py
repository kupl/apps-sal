class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        cache = {}
        def drop(egg, floor):
            if egg==1 or floor<=1:
                return floor
            if (egg, floor) in cache:
                return cache[(egg, floor)]
            minAttempts = float('inf')
            l=1;h=floor
            while l<=h:
                mid = (l+h)//2
                low = drop(egg-1, mid-1)
                high = drop(egg, floor-mid)
                attempts = 1 + max(low, high)
                if low<high:
                    l=mid+1
                else:
                    h=mid-1
                minAttempts = min(minAttempts, attempts)
            cache[(egg, floor)] = minAttempts
            return minAttempts
        return drop(K, N)
