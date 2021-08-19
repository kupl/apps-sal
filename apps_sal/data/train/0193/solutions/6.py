from collections import defaultdict
from collections import OrderedDict


class Solution:

    def createCount(self, arr):
        res = defaultdict(lambda: 0)
        for num in arr:
            res[num] += 1
        res = sorted(list(res.items()), key=lambda x: x[1], reverse=True)
        res = collections.OrderedDict(res)
        return res

    def minSetSize(self, arr: List[int]) -> int:
        total = 0
        num = 0
        res = self.createCount(arr)
        for key in res:
            if total >= len(arr) // 2:
                return num
            total += res[key]
            num += 1
        return num
