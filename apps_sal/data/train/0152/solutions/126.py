class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort balls
        position.sort()
        # max number of balls that can preserve a min difference of diff between any two balls

        def count_balls(diff):
            nballs, cur = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= diff:
                    nballs += 1
                    cur = position[i]
            return nballs
        # m can range from 1 to position[-1] - position[0]
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if count_balls(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1

        return right
