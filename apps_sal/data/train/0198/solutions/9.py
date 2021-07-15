class Solution:
    def equalSubstring(self, s, t, maxCost):
        n = len(s)
        right = 0
        nowSum = 0
        res = 0
        for left in range(n):
            while right <= n - 1 and nowSum + abs(ord(s[right]) - ord(t[right])) <= maxCost: 
                nowSum += abs(ord(s[right]) - ord(t[right]))
                right += 1
            res = max(res, right - left)
            nowSum -= abs(ord(s[left]) - ord(t[left]))
        return res          
