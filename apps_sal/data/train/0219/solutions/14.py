class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        bits = [1 if x > 8 else -1 for x in hours]
        pref = [0] * (len(bits) + 1)
        for i in range(1, len(bits) + 1):
            pref[i] = pref[i - 1] + bits[i - 1]
        ans = 0
        min_val = len(bits) + 1
        for y in sorted(enumerate(pref), key=lambda x: (x[1], -x[0])):
            min_val = min(min_val, y[0])
            ans = max(ans, y[0] - min_val)
        return ans
