class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        st = [0] * (hi + 1 - lo)
        std = {}
        for x in range(lo, hi + 1):
            i = x
            while x != 1:
                st[i - lo] += 1
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = 3 * x + 1
            if st[i - lo] in list(std.keys()):
                std[st[i - lo]].append(i)
            else:
                std[st[i - lo]] = [i]
        s_val = sorted(list(std.keys()))
        ans = std[s_val[0]]
        for i in range(1, len(s_val)):
            ans = ans + std[s_val[i]]
        return ans[k - 1]
