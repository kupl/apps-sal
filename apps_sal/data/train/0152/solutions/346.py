class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isFeasible(positions, mid, k): 
            taken = 1
            last = positions[0]
            for i in range(1, len(positions)):
                if positions[i] - last >= mid:
                    taken += 1
                    last = positions[i]
            return taken >= k
        
        def largestMinDist(positions, n, k): 
            low = 0
            high = max(positions) - min(positions) + 1
            while high - low > 1:
                mid = (low + high) // 2
                if isFeasible(positions, mid, k):
                    low = mid
                else:
                    high = mid
            return low
        
        n = len(position) 
        
        position = sorted(position)
        
        '''
        if m == len(position):
            ans = max(position) - min(position)
            for i in range(1, n):
                diff = position[i] - position[i - 1]
                if diff < ans:
                    ans = diff
            return ans
        '''
    
        return largestMinDist(position, n, m)
