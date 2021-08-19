import math


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        max_possible_answer = (position[-1] - position[0]) // (m - 1)  # 3

        # linear search - time limit exceed
        # for i in range(1,1+max_possible_answer):
        #     if not self.is_possible( position, m, i):
        #         break
        # return i-1

        # binary search
        l = 1
        r = max_possible_answer + 1
        # T T T T T F F -> want to know last T
        # similar to 278
        while l < r:
            # why + 1?? because we use l = mid (inclusive) if we don't round up
            # it will get stuck
            # mid = (r+l) // 2  + 1
            mid = math.ceil((r + l) / 2)
            if self.is_possible(position, m, mid):
                l = mid  # mid may be answer
            else:
                r = mid - 1  # mid can't be answer
        return l

    def is_possible(self, position, m, gap):
        i = 1
        prev = position[0]
        m -= 1
        while i < len(position) and m > 0:
            if position[i] - prev >= gap:
                m -= 1
                prev = position[i]
            else:
                i += 1

        return m == 0
