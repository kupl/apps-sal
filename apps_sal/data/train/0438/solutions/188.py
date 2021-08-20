class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        dp = [(-1, -1)] * (len(arr) + 1)
        groups = collections.defaultdict(int)
        if len(arr) == 1:
            return 1
        res = -1
        for (i, a) in enumerate(arr):
            (leftPos, rightPos) = (a, a)
            if a == 1:
                rightPos = a if dp[a + 1][1] == -1 else dp[a + 1][1]
            elif a == len(arr):
                leftPos = a if dp[a - 1][0] == -1 else dp[a - 1][0]
            else:
                leftPos = a if dp[a - 1][0] == -1 else dp[a - 1][0]
                rightPos = a if dp[a + 1][1] == -1 else dp[a + 1][1]
            dp[a] = (leftPos, rightPos)
            dp[leftPos] = (leftPos, rightPos)
            dp[rightPos] = (leftPos, rightPos)
            groups[rightPos - leftPos + 1] += 1
            groups[a - leftPos] -= 1
            groups[rightPos - a] -= 1
            if groups[m] >= 1:
                res = i + 1
        return res
