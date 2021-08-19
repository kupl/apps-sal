class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]
        print(position)
        (left, right) = (1, position[-1] - position[0])

        def valid(mid):
            count = 1
            last = position[0]
            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    last = position[i]
                    count += 1
            return count >= m
        while left < right:
            mid = (right - left + 1) // 2 + left
            if valid(mid):
                left = mid
            else:
                right = mid - 1
        return left
