from functools import lru_cache


class Solution:

    def stoneGameIII(self, s: List[int]) -> str:
        nums = len(s)

        @lru_cache(maxsize=10000)
        def helper(index, first):
            r = nums - index
            if r == 0:
                return (0, 0)
            if r == 1:
                if first:
                    return (s[-1], 0)
                else:
                    return (0, s[-1])
            if r == 2:
                (x, y) = s[-2:]
                if 0 <= x and 0 <= y or (x < 0 and y > 0):
                    if first:
                        return (x + y, 0)
                    return (0, x + y)
                if first:
                    return (x, y)
                return (y, x)
            (a1, b1) = helper(index + 1, not first)
            (a2, b2) = helper(index + 2, not first)
            (a3, b3) = helper(index + 3, not first)
            if first:
                a1 += s[index]
                a2 += sum(s[index:index + 2])
                a3 += sum(s[index:index + 3])
            else:
                b1 += s[index]
                b2 += sum(s[index:index + 2])
                b3 += sum(s[index:index + 3])
            choices = [(a1, b1), (a2, b2), (a3, b3)]
            if first:
                return max(choices)
            return min(choices)
        (a, b) = helper(0, True)
        if a == b:
            return 'Tie'
        if a < b:
            return 'Bob'
        return 'Alice'
