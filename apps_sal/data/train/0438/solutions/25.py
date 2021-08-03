from collections import defaultdict
from typing import *
from bisect import *


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        Start = dict()
        End = dict()
        NumWithSize = defaultdict(int)
        for i in range(n):
            NumWithSize[0] += 1
        step = 0
        res = -1
        for x in arr:
            step += 1
            x -= 1
            NumWithSize[0] -= 1
            if (x - 1) in End:
                leftSize = End[x - 1] - Start[x - 1] + 1
                NumWithSize[leftSize] -= 1
                if (x + 1) in End:
                    rightSize = End[x + 1] - Start[x + 1] + 1
                    NumWithSize[rightSize] -= 1
                    NumWithSize[leftSize + rightSize + 1] += 1
                    Start[End[x + 1]] = Start[x - 1]
                    End[Start[x - 1]] = End[x + 1]
                else:
                    # only merge with left
                    NumWithSize[leftSize + 1] += 1
                    Start[x] = Start[x - 1]
                    End[x] = x
                    End[Start[x - 1]] = x
            elif (x + 1) in End:
                # only merge with right
                rightSize = End[x + 1] - Start[x + 1] + 1
                NumWithSize[rightSize] -= 1
                NumWithSize[rightSize + 1] += 1
                Start[x] = x
                End[x] = End[x + 1]
                Start[End[x + 1]] = x
            else:
                # make only 1 block siez
                NumWithSize[1] += 1
                Start[x] = End[x] = x
            if NumWithSize[m] > 0:
                res = step
        return res


print((Solution().findLatestStep(arr=[3, 5, 1, 2, 4], m=1)))  # 4
print((Solution().findLatestStep(arr=[3, 1, 5, 4, 2], m=2)))  # -1
print((Solution().findLatestStep(arr=[1], m=1)))  # 1
print((Solution().findLatestStep(arr=[2, 1], m=2)))  # 2
