class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        arr = []
        lim = len(s)
        for i in range(0, lim):
            arr.append(abs(ord(s[i]) - ord(t[i])))

        sm = [arr[0]]

        for j in range(1, lim):
            sm.append(sm[-1] + arr[j])

        l = 0
        h = lim

        mx = 0
        while l <= h:
            m = (l + h) // 2
            t = 0
            for i in range(0, lim - m):
                if sm[i + m] - sm[i] + arr[i] <= maxCost:
                    t = 1
                    break
            if t == 1:
                if m + 1 > mx:
                    mx = m + 1
                l = m + 1
            else:
                h = m - 1
        return mx
