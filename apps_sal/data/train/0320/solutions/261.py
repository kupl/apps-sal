class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # print(nums)

        ops = 0

        if not any(n != 0 for n in nums):
            return 0

        while nums:
            if any((n % 2 != 0) for n in nums):
                # print(\"Not all even\")
                for idx, n in enumerate(nums):
                    # print(\"iterating on idx={} and n={}\".format(idx, n))
                    if nums[idx] % 2 != 0:
                        nums[idx] -= 1
                        ops += 1
                nums = [n for n in nums if n != 0]
                # print(nums)
            else:
                # print(\"All even\")
                ops += 1
                nums = [int(n / 2) for n in nums]
                # print(nums)

        return ops
