class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position = sorted(position)
        res = 0

        def check(n):
            count = 0
            cur = -1
            for i in range(len(position)):
                if cur < 0:
                    cur = position[i]
                    continue
                if position[i] - cur >= n:
                    cur = position[i]
                    count += 1
            return count + 1

        l, r = 0, position[-1] - position[0]

        while l <= r:
            mid = (l + r) // 2

            if check(mid) >= m:
                res = max(mid, res)
                l = mid + 1

            else:
                r = mid - 1

        return res
