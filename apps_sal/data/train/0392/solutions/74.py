import math


class Solution:
    def numWays(self, s: str) -> int:
        dict1 = dict()
        cur = 0
        for i in range(len(s)):
            if(s[i] == '1'):
                dict1[cur + 1] = i
                cur += 1
        if(cur % 3 != 0):
            return 0
        if(cur == 0):
            len_s = len(s) - 1
            return (math.factorial(len_s) // (math.factorial(len_s - 2) * math.factorial(2))) % (10**9 + 7)

        div = cur // 3
        return ((dict1[div + 1] - dict1[div]) * (dict1[div * 2 + 1] - dict1[div * 2])) % (10**9 + 7)
