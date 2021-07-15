class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def foo( d):
            ans = 1; last = position[0]
            for i in range( 1, len( position)):
                if position[i] - last >= d:
                    ans += 1
                    last = position[i]
            return ans
        
        left = 0; right = position[-1] - position[0]

        while left < right:
            mid = right - ( right - left) // 2
            if foo( mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left
