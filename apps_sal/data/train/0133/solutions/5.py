from sys import maxsize
from collections import Counter


class Solution:

    def balancedString(self, s):
        n = len(s)
        right = 0
        chars = Counter(s)
        res = maxsize
        for left in range(n):
            while right <= n - 1 and any((chars[c] > n // 4 for c in 'QWER')):
                chars[s[right]] -= 1
                right += 1
            if all((chars[c] <= n // 4 for c in 'QWER')):
                res = min(res, right - left)
            chars[s[left]] += 1
        return res
