class Solution:

    def numSub(self, s: str) -> int:
        sum = cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
                sum = (sum + cnt) % (10 ** 9 + 7)
            else:
                cnt = 0
        return sum
