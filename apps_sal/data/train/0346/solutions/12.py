class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        data = []
        curr = 0
        L = 0
        count = 0
        for num in nums:
            if num % 2 == 0:
                curr += 1
            else:
                L += 1
                data.append(curr)
                curr = 0
        if L < k:
            return 0
        end = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 1:
                break
            end += 1
        for i in range(k - 1, L - 1):
            count += (data[i - k + 1] + 1) * (data[i + 1] + 1)
        return count + (end + 1) * (data[-k] + 1)
