from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = defaultdict(int)
        for a in arr:
            d[a % k] += 1
        res = True
        for i in range(1, (k+1)//2):
            print(i, k)
            if d[i] != d[k-i]:
                res = False
        if d[0] % 2 != 0:
            res = False
        if k % 2 == 0 and d[k//2] % 2 != 0:
            res = False
        return res
