class Solution:

    def minDays(self, n: int) -> int:
        dp = [n, n, n]
        last = set([n])

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
            if any((n == 0 for n in last)):
                return i
        return n
