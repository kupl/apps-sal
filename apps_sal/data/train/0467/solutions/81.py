class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        valAll = 0
        for num in nums:
            local = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    local.add(i)
                    local.add(int(num / i))
                    if len(local) > 4:
                        break
            if len(local) == 4:
                valAll += sum(local)
        return valAll
