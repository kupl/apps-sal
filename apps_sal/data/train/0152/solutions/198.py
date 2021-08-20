class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (left, right) = (0, position[-1] - position[0])

        def check(dist):
            pre = position[0]
            n = m - 1
            i = 1
            while n:
                while i < len(position) and position[i] - pre < dist:
                    i += 1
                if i >= len(position):
                    return False
                pre = position[i]
                i += 1
                n -= 1
            return True
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
