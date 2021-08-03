class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            cnt = 0
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    cnt += 1
                    d = i
                if cnt > 1:
                    break
            if cnt == 1 and d != num // d:
                ans += 1 + d + num // d + num
        return ans
