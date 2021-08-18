class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def isOK(x):
            rest = m - 1
            pre = position[0]
            for p in position[1:]:
                if p - pre >= x:
                    pre = p
                    rest -= 1
                    if rest == 0:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if isOK(mid):
                left = mid
            else:
                right = mid - 1
        return right
