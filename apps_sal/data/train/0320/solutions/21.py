import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 4,2,5->2,1,2->2,0,2->1,0,1
        # 1,5->1,4->1,2->1,1
        # 2,4,8,16->1,2,4,4->
        count = max([int(math.log(x) / math.log(2)) for x in nums if x > 0])
        for n in nums:
            while (n):
                if n % 2:
                    count += 1
                    n -= 1
                else:
                    n //= 2
        return count
