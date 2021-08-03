class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if not nums:
            return 0
        dic = {0: [-1]}
        if nums[0] % p not in dic:
            dic[nums[0] % p] = []
        dic[nums[0] % p] = [0]

        nums[0] = nums[0] % p
        for i in range(1, len(nums)):
            nums[i] = (nums[i] + nums[i - 1]) % p
            if nums[i] not in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)

        if nums[-1] == 0:
            return 0
        output = len(nums)
        for i in range(len(nums)):
            res = (nums[i] - nums[-1]) % p
            try:
                output = min(output, min([i - j for j in dic[res] if j < i]))
            except:
                continue

        return output if output != len(nums) else -1
