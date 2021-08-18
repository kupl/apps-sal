

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        distance = [0 for _ in range(len(position) - 1)]
        for i in range(len(position) - 1):
            diff = position[i + 1] - position[i]
            distance[i] = diff
        left = min(distance)
        right = position[-1] - position[0]

        def check(diff, m):
            m -= 1
            pre_dis = 0
            for i in range(0, len(distance)):
                if distance[i] + pre_dis >= diff:
                    m -= 1
                    if m <= 0:
                        return True
                    pre_dis = 0
                else:
                    pre_dis += distance[i]
            return False

        while left < right:
            mid = (left + right + 1) // 2
            if check(mid, m) == True:
                left = mid
            else:
                right = mid - 1

        return left
