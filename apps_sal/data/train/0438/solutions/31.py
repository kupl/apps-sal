from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        s = [0 for _ in arr]
        ans = -1
        for i, n in enumerate(arr):
            num = n - 1
            left = s[num - 1] if num > 0 else 0
            right = s[num + 1] if num < len(s) - 1 else 0
            total = left + right + 1
            s[num - left] = total
            s[num + right] = total
            if left == m or right == m:
                ans = i
        if m == max(s):
            return i + 1
        return ans
