class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (left, right) = (0, position[-1] - position[0])
        while left <= right:
            mid = (left + right) // 2
            count = 1
            curr = position[0]
            for x in position[1:]:
                if x - curr >= mid:
                    count += 1
                    curr = x
            if count >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right
