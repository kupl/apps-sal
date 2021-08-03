class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        out = 0
        for i in nums:
            temp = set()
            for j in range(1, floor(sqrt(i)) + 1):
                if i % j == 0:
                    temp.add(j)
                    temp.add(int(i / j))
                if len(temp) > 4:
                    break
            if len(temp) == 4:
                out += sum(temp)
        return out
