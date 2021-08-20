class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def four_divisors(n):
            div = set()
            cnt = 0
            sums = 0
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    div.add(i)
                    sums += i
                    div.add(n // i)
                    sums += n // i
                    cnt += 2
                    if cnt > 4:
                        return 0
            return sums if len(div) == 4 else 0
        if not nums:
            return 0
        nums.sort()
        total = 0
        past = [None, None]
        for (i, v) in enumerate(nums):
            if i > 0 and v == nums[i - 1] and (v == past[0]):
                total += past[1]
                continue
            tmp = four_divisors(v)
            total += tmp
            past = [v, tmp]
        return total
