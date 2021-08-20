class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        pSieve = [0 for k in range(10 ** 5 + 1)]
        for k in range(2, len(pSieve)):
            if pSieve[k] == 1:
                continue
            pSieve[k + k::k] = [1] * ((len(pSieve) - 1) // k - 1)
        for num in nums:
            if num == 1 or pSieve[num] == 0 or sqrt(num) == int(sqrt(num)):
                continue
            k = 2
            while num % k != 0:
                k += 1
            if num == k ** 3 or pSieve[num // k] == 0:
                total += 1 + num + k + num // k
        return total
