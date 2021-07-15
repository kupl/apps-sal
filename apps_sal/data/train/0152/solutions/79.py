class Solution:
    def put(self, position, d, m):
        n = 1
        curr = position[0]
        for i in range(1, len(position)):
            if position[i] - curr >= d:
                n += 1
                curr = position[i]
            if n >= m:
                return 1
        return 0
    
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 0, position[-1]
        
        while low < high:
            mid = (high + low + 1) // 2
            comp = self.put(position, mid, m)
            
            if comp > 0:
                low = mid
            else:
                high = mid - 1
        return low
