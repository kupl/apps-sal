class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count_d(dis):
            ans, cur = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= dis:
                    ans += 1
                    cur = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r-l)//2
            if count_d(mid) >= m:
                l = mid 
            else:
                r = mid - 1
        return l
