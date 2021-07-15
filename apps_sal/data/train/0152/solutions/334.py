class Solution:
    def maxDistance(self, positions: List[int], m: int) -> int:
        positions.sort()
        # try to add balls and record the position
        def check(mid):
            p = 0
            count = 0
            for q in range(len(positions)):
                if positions[q] - positions[p] >= mid:
                    p = q
                    count += 1
            return count >= m-1                  
        
        low, high = 0, positions[-1]-positions[0]
        # print(low, high)
        
        res = 0
        
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                low = mid + 1
                res = max(res, mid)
            else:
                high = mid - 1
        return res
