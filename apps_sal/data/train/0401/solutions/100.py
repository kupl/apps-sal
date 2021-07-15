def maxsum(a, k):
    dp =[float('-inf') if a[0]%k!=x else a[0] for x in range(k)]
    for i in range(1, len(a)):
        new = [0 for x in range(k)]
        for j in range(k):
            rem=a[i]%k
            index = (k-rem+j)%k
            new[j] = max(dp[j], dp[index]+a[i], a[i] if a[i]%k==j else float('-inf'))
        dp = new

    return 0 if dp[0] ==float('-inf') else dp[0]

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        return maxsum(nums, 3)
