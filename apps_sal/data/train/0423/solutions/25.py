class Solution:

    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        indexMap = defaultdict(list)
        dp = [0] * len(arr)
        maxSeq = 0
        for (i, num) in enumerate(arr):
            if num - diff in indexMap:
                for newIndex in indexMap[num - diff]:
                    dp[i] = max(dp[i], dp[newIndex])
            dp[i] += 1
            maxSeq = max(maxSeq, dp[i])
            indexMap[num].append(i)
        return maxSeq
