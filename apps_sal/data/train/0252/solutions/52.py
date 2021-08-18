class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        needed = [100000] * (n + 1)

        for i in range(len(ranges)):
            l_i = i - ranges[i]

            if l_i <= 0:
                need = 1
            else:
                need = needed[l_i] + 1

            right_most = min(i + ranges[i], len(ranges) - 1)

            while need < needed[right_most] and right_most > i - 1:
                needed[right_most] = need
                right_most -= 1

        if needed[-1] > 10000:
            return -1

        return needed[-1]
