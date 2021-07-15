class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            divs = set()
            i = 1
            while i ** 2 <= num:
                if not num % i:
                    divs.add(i)
                    divs.add(num // i)
                if len(divs) > 4:
                    break
                i += 1
            if len(divs) == 4:
                ret += sum(divs)
        return ret
