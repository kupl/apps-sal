class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += self.fourDivisors(num)
        return ans

    def fourDivisors(self, num):
        memo = set()
        for i in range(1, num + 1):
            if i * i > num:
                break
            if num % i == 0:
                memo.add(i)
                memo.add(num // i)
                if len(memo) > 4:
                    return 0
        if len(memo) == 4:
            return sum(memo)
        return 0
