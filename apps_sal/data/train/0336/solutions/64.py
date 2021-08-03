class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sFreq = dict()
        for char in s:
            try:
                sFreq[char] += 1
            except:
                sFreq[char] = 1
        ans = 0
        for char in t:
            if char in sFreq and sFreq[char] > 0:
                sFreq[char] -= 1
            else:
                ans += 1
        return ans
