class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        if m == 2:
            return position[-1] - position[0]

        def checkPossible(ans0):
            preV = position[0]
            leftM = m - 1
            for num in position[1:]:
                if num - preV >= ans0:
                    leftM -= 1
                    preV = num
                    if leftM == 0:
                        return True
            return False
        l = 0
        r = position[-1]
        ans = position[1] - position[0]
        while r > l:
            mid = (r + l) // 2
            if checkPossible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans
