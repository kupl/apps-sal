class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        res = 0
        c = [0] * (len(s) + 1)
        j = 0
        for i in range(1, len(s) + 1):
            c[i] += c[i - 1] + abs(ord(s[i - 1]) - ord(t[i - 1]))

            while c[i] > maxCost:
                c[i] -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            res = max(res, i - j)
        return res
