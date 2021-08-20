from collections import defaultdict
from operator import itemgetter


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_dict = defaultdict(int)

        def cal_power(n):
            nonlocal power_dict
            if n in list(power_dict.keys()):
                return power_dict[n] - 1
            if n == 1:
                return 0
            if n % 2 == 0:
                n = n / 2
            elif n % 2 == 1:
                n = 3 * n + 1
            power_dict[n] = cal_power(n) + 1
            return power_dict[n]
        lst = []
        for i in range(lo, hi + 1):
            lst.append((cal_power(i), i))
        lst = sorted(lst, key=itemgetter(0))
        return lst[k - 1][1]
