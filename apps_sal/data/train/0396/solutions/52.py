class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        c = 1
        p = 1
        if k < 0:
            return '-1'

        elif k % 2 == 0 or k % 5 == 0:
            return -1

        else:
            while c:
                if c % k == 0:
                    return p

                c = c * 10 + 1
                p = p + 1
