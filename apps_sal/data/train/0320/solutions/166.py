class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        ops = 0

        n = len(nums)

        while nums:
            # print(nums)
            while nums[-1] == 0:
                nums.pop()
                if not nums:
                    break
                n -= 1
            if not nums:
                break

            oc = 0

            for i in range(n):
                if nums[i] % 2 != 0:
                    oc = 1
                    break

            if oc == 1:
                for i in range(n):
                    if nums[i] % 2 != 0:
                        ops += 1
                        nums[i] -= 1
            else:
                ops += 1
                for i in range(n):
                    nums[i] = nums[i] // 2
        return ops
