class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def num_balls(min_dist: int) -> int:
            ans, curr = 1, 0

            for i in range(1, n):
                if position[i] - position[curr] >= min_dist:
                    ans += 1
                    curr = i
            return ans

        l, r = 0, position[n - 1] - position[0]

        while l < r:
            mid = r - (r - l) // 2

            if num_balls(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
