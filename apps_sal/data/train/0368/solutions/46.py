class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort(reverse = True)
        maxi = 0
        for i in range(len(s)):
            t = 0
            for j in range(i+1):
                t += s[j]*(i+1-j)
            maxi =max(maxi,t)
        return maxi
