class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # 10:58 9/24/20
        def four_divisors3(n):
            div = set()
            i = 1
            while i * i < n:
                if n % i == 0:
                    div.add(i)
                    div.add(n // i)
                    if len(div) > 4:
                        return 0
                i += 1
            return sum(div) if len(div) == 4 else 0

        def four_divisors(n):
            div = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    div.add(i)
                    div.add(n // i)
                    if len(div) > 4:
                        return 0
            return sum(div) if len(div) == 4 else 0

        def four_divisors2(n):
            cnt = 0
            sums = 0
            div = set()
            if n != 0:
                # i = 1
                for i in range(1, int(n ** 0.5) + 1):
                    if n % i == 0:
                        cnt += 2
                        sums += i + n // i
                        # div.add(i)
                        # div.add(n // i)
                    if cnt > 4:
                        return 0
                    # i += 1
            return sums if cnt == 4 else 0

        if not nums:
            return 0
        nums.sort()
        total = 0
        # sums = [0]
        past = [None, None]

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1] and v == past[0]:
                total += past[1]
                continue
            tmp = four_divisors(v)
            total += tmp
            past = [v, tmp]

        return total
