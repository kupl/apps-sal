class Solution:
    def minDays(self, n: int) -> int:
        dp = [n, n, n]
        last = set([n])
        # dp = [[n] * 3 for _ in range(n+1)]

        def min_2(nums):
            xs = [x for x in nums if x % 2 == 0]
            if not xs:
                return min(nums)
            return min(xs) // 2

        def min_3(nums):
            xs = [x for x in nums if x % 3 == 0]
            if not xs:
                return min(nums)
            return min(xs) // 3

        for i in range(1, n + 1):
            curr = set()
            for n in last:
                curr.add(n - 1)

            for n in last:
                if n % 2 == 0:
                    curr.add(n // 2)

            for n in last:
                if n % 3 == 0:
                    curr.add(n // 3)

            last = last | curr
            # print(last)
            if any(n == 0 for n in last):
                return i
            # dp[0] = min(last) - 1
            # dp[1] = min_2(last)
            # dp[2] = min_3(last)
            # print(dp, last)
            # if any(dp[i] == 0 for i in range(3)):
            #     return i
            # for d in dp:
            #     last.add(d)
            # dp = dp[:]
        # print('-' * 20)
        return n
