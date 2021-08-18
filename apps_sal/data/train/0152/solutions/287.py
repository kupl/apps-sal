class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        L = len(position)

        left = 1
        right = position[-1] - position[0]

        def can_place(f):
            n_ball = m - 1
            cum_dis = 0
            p = 1
            while n_ball > 0 and p < L:
                cum_dis += position[p] - position[p - 1]
                if cum_dis >= f:
                    n_ball -= 1
                    cum_dis = 0
                p += 1

            if n_ball == 0:
                return True
            else:
                return False

        while left < right:
            mid = right - (-left + right) // 2
            if can_place(mid):
                left = mid
            else:
                right = mid - 1

        return left
