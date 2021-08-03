class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        z = 0
        for num in nums:
            i = 1
            res = []

            while i * i <= num:
                if (num % i == 0):
                    res.append(i)
                i += 1
            if len(res) == 2:
                lin = [num // j for j in res]
                final = list(set(res + lin))
                if (len(final) == 4):
                    z += sum(final)

        return max(0, z)
