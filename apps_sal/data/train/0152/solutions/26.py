class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def helper(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        left, right = 0, position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            if helper(mid) < m:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1
