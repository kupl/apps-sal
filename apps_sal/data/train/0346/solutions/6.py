class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        mp = defaultdict(int)
        mp[0] = 1
        csum, ans = 0, 0

        for i, num in enumerate(nums):
            csum += num
            ans += mp[csum - k]
            mp[csum] += 1

        return ans
