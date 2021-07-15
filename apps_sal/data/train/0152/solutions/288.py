class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 1, position[-1]-position[0]
        while l<r:
            mid = l+(r-l+1)//2
            placefind = 1
            preIndex = 0
            for i in range(1, len(position)):
                if position[i]-position[preIndex]>=mid:
                    placefind += 1
                    preIndex = i
            if placefind >= m:
                l = mid
            else:
                r = mid-1
        return l
