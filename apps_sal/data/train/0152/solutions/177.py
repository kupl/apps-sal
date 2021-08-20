class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(dis):
            num = 0
            presum = 0
            for i in range(1, n):
                presum += position[i] - position[i - 1]
                if presum >= dis:
                    presum = 0
                    num += 1
            return num
        (l, r) = (0, position[-1] - position[0])
        while l < r - 1:
            mid = (l + r) // 2
            if check(mid) >= m - 1:
                l = mid
            else:
                r = mid - 1
        return r if check(r) >= m - 1 else l
