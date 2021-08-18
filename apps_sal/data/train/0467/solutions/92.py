class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def four_divisors(n):
            cnt = 0
            div = set()
            if n != 0:
                i = 1
                for i in range(1, int(n ** 0.5) + 1):
                    if n % i == 0:
                        cnt += 2
                        div.add(i)
                        div.add(n // i)
                    if len(div) > 4:
                        return 0
            return sum(div) if len(div) == 4 else 0

        if not nums:
            return 0
        nums.sort()
        total = 0
        past = [None, None]

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1] and v == past[0]:
                total += past[1]
                continue
            tmp = four_divisors(v)
            total += tmp
            past = [v, tmp]

        return total
