class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dp = [(-1, -1)] * (len(arr) + 1)
        groups = collections.defaultdict(int)
        if len(arr) == 1:
            return 1
        res = -1
        for i, a in enumerate(arr):
            left, right = -1, -1
            if a == 1:
                right = a + 1
            elif a == len(arr):
                left = a - 1
            else:
                left = a - 1
                right = a + 1
            leftPos = a if left == -1 or dp[left][0] == -1 else dp[left][0]
            rightPos = a if right == -1 or dp[right][1] == -1 else dp[right][1]

            dp[a] = (leftPos, rightPos)
            if leftPos != a:
                dp[leftPos] = (leftPos, rightPos)
            if rightPos != a:
                dp[rightPos] = (leftPos, rightPos)

            groups[rightPos - leftPos + 1] += 1
            groups[a - leftPos] -= 1
            groups[rightPos - a] -= 1
            if groups[m] >= 1:
                res = i + 1
        return res
