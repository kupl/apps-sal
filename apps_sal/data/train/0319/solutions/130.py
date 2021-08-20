class Solution:

    def stoneGameIII(self, s: List[int]) -> str:
        i_1 = i_2 = i_3 = 0
        i = len(s) - 1
        while i >= 0:
            ans = -sys.maxsize
            ans = max(ans, s[i] - i_1)
            if i + 1 < len(s):
                ans = max(ans, s[i] + s[i + 1] - i_2)
            if i + 2 < len(s):
                ans = max(ans, s[i] + s[i + 1] + s[i + 2] - i_3)
            i_3 = i_2
            i_2 = i_1
            i_1 = ans
            i -= 1
        a = i_1
        if a > 0:
            return 'Alice'
        if a == 0:
            return 'Tie'
        return 'Bob'
