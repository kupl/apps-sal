class Solution:
    def find_divisors(self, num):
        cnt = 0
        run_sum = num + 1
        for i in range(2, int(num**0.5) + 1):
            if i * i == num:
                return 0
            if cnt > 1:
                return 0
            if not num % i:
                run_sum += num // i + i
                cnt += 1
        return run_sum if cnt == 1 else 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            cnt += self.find_divisors(i)
        return cnt
