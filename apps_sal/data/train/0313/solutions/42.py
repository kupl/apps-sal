from collections import Counter
from heapq import *


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k * m > len(bloomDay):
            return -1

        que = [[-1 * num, ind] for ind, num in enumerate(bloomDay[:k])]
        heapify(que)

        maxArr = [-1 * que[0][0]]
        for ind in range(k, len(bloomDay)):
            while que and que[0][1] <= ind - k:
                heappop(que)
            heappush(que, [-1 * bloomDay[ind], ind])
            maxArr.append(-1 * que[0][0])

        def isValid(num):
            cnt = 0
            ind = 0
            while ind < len(maxArr):
                if maxArr[ind] <= num:
                    cnt += 1
                    ind += k
                else:
                    ind += 1
            return cnt >= m

        low = 1
        high = max(bloomDay) + 1
        ans = -1
        while low < high:
            mid = low + (high - low) // 2
            if isValid(mid):
                high = mid
                ans = mid
            else:
                low = mid + 1
        return ans
