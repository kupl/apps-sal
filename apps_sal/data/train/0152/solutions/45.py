class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def isfail(mid):
            ans = 1
            curr = position[0]  # alike greedy idea, we just put the first ball at position 0!
            for i in range(1, n):
                if position[i] - curr >= mid:
                    ans += 1
                    curr = position[i]
            return ans < m

        left = 0  # 注意，不应该把left赋值为min(position)! 因为我们求得是distance!
        # note that, left = min(position) is wrong, since we are looking for 'distance'!
        right = max(position) - min(position) + 1
        while left < right:
            mid = left + (right - left) // 2
            if isfail(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1  # left is the min value to fail, so left-
