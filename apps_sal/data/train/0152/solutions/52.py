class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def count(d):
            ans = 1
            pre_pos = position[0]
            for i in range(1, n):
                if position[i] - pre_pos >= d:
                    ans += 1
                    pre_pos = position[i]
            return ans
        n = len(position)
        position.sort()
        left = 1
        right = position[-1] - position[0]
        while left < right:
            mid = left + (right - left + 1) // 2
            if count(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left
