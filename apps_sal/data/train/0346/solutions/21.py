class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        If we replace the odds with 1's and evens with 0's then the problem 
        is similar to finding number of subarrays with sum = k
        '''
        '''
        dp = collections.defaultdict(int)
        dp[0] = 1
        cur = 0
        result = 0
        for i in range(len(nums)):
            cur += nums[i]%2
            diff = cur-k
            if diff in dp:
                result += dp[diff]
            dp[cur]+=1
        
        return result
        '''
        def atMost(k):
            l, result = 0, 0
            for i in range(len(nums)):
                k -= nums[i] % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                result += i - l + 1
            return result

        return atMost(k) - atMost(k - 1)
