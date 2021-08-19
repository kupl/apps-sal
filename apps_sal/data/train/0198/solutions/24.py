class Solution:

    def equalSubstring(self, s, t, maxCost):
        cost = 0
        ans = 0
        (left, right) = (0, -1)
        for (s_c, t_c) in zip(s, t):
            right += 1
            cost += abs(ord(s_c) - ord(t_c))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
