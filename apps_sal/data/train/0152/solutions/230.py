class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        arr = sorted(position)
        
        if m == 2:
            return arr[-1] - arr[0]
        
        def is_possible(f):
            count = 1
            origin = arr[0]
            for i in range(1, n):
                if arr[i] - origin >= f:
                    count += 1
                    origin = arr[i]
                if count >= m:
                    return True
            
            if count < m - 1 or arr[-1] - origin < f:
                return False
            
            return True
        
        low, high = 1, arr[-1] - arr[0]
        
        while low + 1 < high:
            f = ceil((high + low) / 2)
            if is_possible(f):
                low = f
            else:
                high = f

        if is_possible(high):
            return high
        return low

