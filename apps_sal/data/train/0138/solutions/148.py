class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def find_list(nums):
            pos = 0
            neg = 0
            for i in nums:

                if i > 0:
                    pos += 1
                if i < 0:
                    neg += 1

            if (neg % 2 == 0):
                print(len(nums))

            else:
                first = 0
                last = len(nums) - 1

                while first <= last:
                    if nums[first] < 0:
                        nums = nums[first + 1:]
                        break
                    else:
                        first += 1
                    if nums[last] < 0:
                        nums = nums[:last]
                        break
                    else:
                        last -= 1

            return len(nums)

        ans = 0
        zero = 0
        remove = 0
        for i in nums:
            if i == 0:
                zero += 1

        while (zero != 0):
            first = 0
            last = len(nums) - 1

            while first <= last:
                if nums[first] == 0:
                    remove_list = nums[:first]
                    ans = max(ans, find_list(remove_list))

                    nums = nums[first + 1:]
                    break
                else:
                    first += 1
                if nums[last] == 0:
                    remove_list = nums[last + 1:]
                    ans = max(ans, find_list(remove_list))

                    nums = nums[:last]

                    break
                else:
                    last -= 1
            zero = zero - 1

        return max(ans, (find_list(nums)))
