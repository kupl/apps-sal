"""
Time Limited
https://leetcode.com/submissions/detail/406886943/testcase/
"""


class Solution:

    def numTimesAllBlue(self, light):
        (cnt, N) = (0, len(light))
        bulbs = [0] * N
        for (i, pos) in enumerate(light, start=1):
            pos -= 1
            if sum(bulbs[:pos]) == 2 * pos:
                bulbs[pos] = 2
                while pos + 1 < N and bulbs[pos + 1] == 1:
                    bulbs[pos + 1] = 2
                    pos += 1
                if sum(bulbs) == 2 * i:
                    cnt += 1
            else:
                bulbs[pos] = 1
        return cnt


class Solution:

    def numTimesAllBlue(self, light):
        (cnt, seen) = (0, set())
        for v in light:
            seen.add(v)
            if max(seen) == len(seen):
                cnt += 1
        return cnt


class Solution:

    def numTimesAllBlue(self, light):
        cnt = 0
        (maxV, size) = (0, 0)
        for v in light:
            size += 1
            if v > maxV:
                maxV = v
            if maxV == size:
                cnt += 1
        return cnt
