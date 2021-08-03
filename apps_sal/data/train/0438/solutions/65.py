class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n, ans = len(arr), -1
        if m == n:
            return m
        cnts = [0] * (n + 2)
        for i, x in enumerate(arr):
            cl, cr = cnts[x - 1], cnts[x + 1]
            if cl == m or cr == m:
                ans = i
            cnts[x - cl] = cnts[x + cr] = cl + cr + 1
        return ans
