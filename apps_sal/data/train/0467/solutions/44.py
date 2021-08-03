class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        def get_divisor(num):
            val = set()
            i = 1
            while i < math.sqrt(num) + 1:
                if num % i == 0:
                    val.add(i)
                    val.add(num // i)
                if len(val) > 4:
                    return val
                i += 1
            return val

        for num in nums:
            a = get_divisor(num)
            if len(a) == 4:
                ans += sum(a)
        return ans
