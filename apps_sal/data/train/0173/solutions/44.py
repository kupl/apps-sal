from collections import defaultdict


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        d = {i: 0 for i in range(k)}
        for ele in arr:
            d[ele % k] += 1
        for i in range(k):
            if d[0] % 2 != 0:
                return False
            elif i != 0 and d[i] != d[k - i]:
                return False
        return True
