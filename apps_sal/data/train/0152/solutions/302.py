class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def isfail(mid):
            ans = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - curr >= mid:
                    ans += 1
                    curr = position[i]
            return ans < m

        res = float('-inf')
        left = 1
        right = position[-1] - position[0]

        while left <= right:
            mid = (left + right) // 2
            if isfail(mid):
                right = mid - 1
            else:
                left = mid + 1
                res = max(res, mid)
        return res
