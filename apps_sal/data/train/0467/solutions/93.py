from collections import defaultdict
from math import ceil


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        count = defaultdict(set)
        for (j, num) in enumerate(nums):
            for i in range(1, ceil(num ** 0.5) + 1):
                if num % i == 0:
                    count[j, num].update({i, num // i})
                    if len(count[j, num]) > 4:
                        break
        total = 0
        print(count)
        for num in count:
            if len(count[num]) == 4:
                total += sum(count[num])
        return total
