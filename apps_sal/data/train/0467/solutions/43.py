class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n & 1 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 and n % (i + 2) == 0:
                    return False
                i += 6
            return True
        res = 0
        c = 0
        temp = set()
        for i in nums:
            for j in range(1, int(i**.5) + 1):
                if i % j == 0:
                    temp.add(j)
                    temp.add(i // j)
                    if i // j != j:
                        c += 2
                    else:
                        c += 1
            res += sum(temp) if c == 4 else 0
            temp = set()
            c = 0
        return res
