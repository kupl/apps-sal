class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:

        flip, one = 0, 0
        for i in S:
            if i == '1':
                one += 1
            else:
                flip += 1
            flip = min(one, flip)
        return flip
