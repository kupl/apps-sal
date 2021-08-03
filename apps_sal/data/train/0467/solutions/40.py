class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            counter = 1
            divisors = []
            while counter <= sqrt(nums[i]) and len(divisors) < 5:
                if nums[i] % counter == 0:
                    if counter not in divisors:
                        divisors.append(counter)
                    if nums[i] // counter not in divisors:
                        divisors.append(nums[i] // counter)
                counter += 1
            if len(divisors) == 4:
                res += sum(divisors)
            print(divisors)

        return res
