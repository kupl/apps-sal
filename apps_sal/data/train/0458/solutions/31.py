class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # [0,1,2,3,4,5,6]
        # need=3, then cut subarray with sum=3
        # csum[j]-csum[i]==3 or csum[j]==0
        A=nums
        need = sum(A) % p
        dp = {0: -1}
        cur = 0
        res = n = len(A)
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1


