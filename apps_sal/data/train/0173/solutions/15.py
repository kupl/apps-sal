import math


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        moduloclasses = [0] * k
        for n in arr:
            moduloclasses[n % k] += 1

        if k % 2 == 0 and moduloclasses[k // 2] % 2 != 0:
            return False
        if moduloclasses[0] % 2 != 0:
            return False

        for i in range(1, math.ceil(k / 2)):
            if moduloclasses[i] != moduloclasses[k - i]:
                return False

        return True
