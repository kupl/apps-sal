import bisect


class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        (r, l, l_idx) = ([], [], [])
        d = []
        for (i, x) in enumerate(hours):
            if i == 0:
                if x > 8:
                    d.append(1)
                else:
                    d.append(-1)
            elif x > 8:
                d.append(d[-1] + 1)
            else:
                d.append(d[-1] - 1)
        for (i, x) in enumerate(d):
            while len(r) > 0 and r[-1][0] <= x:
                r.pop()
            r.append((x, i))
            if len(l) == 0 or x < l[-1]:
                l.append(x)
                l_idx.append(i)
        ans = 0
        l.reverse()
        l_idx.reverse()
        for x in r:
            if x[0] > 0:
                ans = max(ans, x[1] + 1)
            else:
                idx = bisect.bisect_right(l, x[0] - 1)
                if idx >= 1:
                    ans = max(ans, x[1] - l_idx[idx - 1])
        return ans
