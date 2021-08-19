# https://leetcode.com/problems/find-latest-group-of-size-m/discuss/836441/Very-Easy

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        # if n==m:
        #     return n

        memo = collections.defaultdict(lambda: 0)
        res = -1
        for idx, i in enumerate(arr):
            left = memo[i - 1]
            right = memo[i + 1]
            if left == m or right == m:
                res = idx
            memo[i - left] = left + right + 1
            memo[i + right] = left + right + 1

        # print (dict(memo))
        if m == memo[1]:
            res = n

        return res
