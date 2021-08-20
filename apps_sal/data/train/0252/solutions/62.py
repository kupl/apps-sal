class Solution:

    def minTaps(self, n: int, ranges):
        taps = [[max(0, i - ranges[i]), min(n, i + ranges[i])] for i in range(n + 1)]
        taps.sort()
        ans = i = last = 0
        while i < len(taps):
            if last == n:
                return ans
            if taps[i][0] > last:
                return -1 if last < n else ans
            temp = -1
            while i < len(taps) and taps[i][0] <= last:
                temp = max(temp, taps[i][1])
                i += 1
            if temp > last:
                ans += 1
                last = temp
            else:
                return -1
        return ans if last == n else -1
