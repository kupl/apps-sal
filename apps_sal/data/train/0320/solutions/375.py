class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Key insight is if nums[i] is odd, there's no way we could have arrived at nums[i]
        # via op 1, i.e. by multiplying by 2 some previous value. So the only way we could
        # have gotten here is by using op 0, nums[i] % 2 times. That is we need to skim off
        # the remainder part that makes it non-even before we can consider using op 1.
        cost = 0
        while True:
            all_zeros = True
            all_evens = True
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue

                all_zeros = False
                if nums[i] % 2 != 0:
                    cost += nums[i] % 2
                    nums[i] = nums[i] - (nums[i] % 2)
                    all_evens = False

            if all_zeros:
                break
            while all_evens:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                    if nums[i] % 2 != 0:
                        all_evens = False
                cost += 1

        return cost
