class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            out = set()

            for i in range(1, int(num ** 0.5+1)):
                a, b = divmod(num, i)
                if b == 0:
                    out.add(i)
                    out.add(a)
                if len(out) > 4: break
            if len(out) == 4:
                ans += sum(out)
        
        return ans
