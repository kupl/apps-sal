class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def div4(i):
            if i <= 5:
                return set()
            else:
                count = {1, i}
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0:
                        count.update({j, i / j})
                    if len(count) > 4:
                        return count
                return count
        count = 0
        for i in nums:
            s = div4(i)
            if len(s) == 4:
                count += sum(s)
        return int(count)
