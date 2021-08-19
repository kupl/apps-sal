class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        If we replace the odds with 1's and evens with 0's then the problem 
        is similar to finding number of subarrays with sum = k
        Space+Time: O(N)
        """
        '\n        dp = collections.defaultdict(int)\n        dp[0] = 1\n        cur = 0\n        result = 0\n        for i in range(len(nums)):\n            cur += nums[i]%2\n            diff = cur-k\n            if diff in dp:\n                result += dp[diff]\n            dp[cur]+=1\n        \n        return result\n        '
        '\n        # of subarrays sum equals k = # of subarrays sum <= k -\n                                      # of subarrays sum <= (k-1)\n        '

        def atMost(k):
            (l, result) = (0, 0)
            for i in range(len(nums)):
                k -= nums[i] % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                result += i - l + 1
            return result

        def atmost(k):
            res = 0
            l = 0
            for i in range(len(nums)):
                k -= nums[i] % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                res += i - l + 1
            return res
        return atmost(k) - atmost(k - 1)
