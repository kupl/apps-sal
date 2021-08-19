class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (1, 10 ** 9)
        while l < r:
            mid = (l + r + 1) // 2
            count = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= mid:
                    count += 1
                    prev = position[i]
            if count >= m:
                l = mid
            else:
                r = mid - 1
        return l
