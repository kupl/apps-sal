class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        max_k = 0
        for value in piles:
            max_k = max(max_k, value)
        
        def possible(k):
            hours = 0
            for item in piles:
                hours += math.ceil(item / k)
                if hours > H:
                    return False
            if hours <= H:
                return True
            return False
        
        def binary_search(low, high):
            mid = low + (high - low)//2
            if possible(low):
                return low
            elif possible(mid):
                return binary_search(low, mid)
            else:
                return binary_search(mid+1, high)
        
        def binary_search_iter(low, high):
            while low < high:
                mid = low + (high - low)//2
                if possible(low):
                    return low
                elif possible(mid):
                    high = mid
                else:
                    low = mid + 1
            return high
        
        return binary_search_iter(1, max_k)
