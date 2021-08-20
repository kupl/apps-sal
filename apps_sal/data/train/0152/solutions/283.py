class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def maxNumberBallsCanBePlaced(minDis):
            count = 1
            end = position[0]
            for i in range(len(position)):
                if position[i] - end >= minDis:
                    end = position[i]
                    count += 1
            return count
        position.sort()
        left = 1
        right = position[-1]
        while left < right:
            mid = left + (right - left) // 2
            if maxNumberBallsCanBePlaced(mid) >= m:
                left = mid + 1
            else:
                right = mid
        return left - 1
