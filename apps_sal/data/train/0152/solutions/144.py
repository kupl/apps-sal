class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def isPossible(dist):
            count = 1
            prev = position[0]
            for x in position[1:]:
                if x - prev >= dist:
                    count += 1
                    prev = x
                    if count == m:
                        return True
            return False
        left, right = 0, position[-1]-position[0]
        while left <= right:
            mid = left + (right-left)//2
            if isPossible(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
