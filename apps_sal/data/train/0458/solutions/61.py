class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        arr = [0]
        for x in nums:
            arr.append((arr[-1] + (x % p)) % p)
        if arr[-1] == 0:
            return 0
        dic = {}
        ans = float('inf')
        i = 0
        while i < len(arr):
            if ((arr[i] - arr[-1]) % p) in dic:
                ans = min(ans, i - dic[(arr[i] - arr[-1]) % p])
            dic[arr[i]] = i
            i += 1
        if ans < len(nums):
            return ans
        return -1
