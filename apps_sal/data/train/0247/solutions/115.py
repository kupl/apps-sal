from collections import *


class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        mapper = defaultdict(int)
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        mapper[0] = -1
        mapper[arr[0]] = 0
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]
            mapper[prefix[i]] = i
        cumu = count = 0
        l = r = None
        ans = float('inf')
        vis = []
        for (i, a) in enumerate(arr):
            cumu += a
            if cumu - target in mapper:
                if l == None:
                    count += 1
                    l = i - mapper[cumu - target]
                    vis.append((mapper[cumu - target] + 1, i))
                else:
                    l = min(l, i - mapper[cumu - target])
            if l != None and cumu + target in mapper:
                ans = min(ans, mapper[cumu + target] - i + l)
        if ans == float('inf'):
            return -1
        return ans
