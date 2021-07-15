from collections import deque
import bisect

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = deque([]), deque([])
        for i, x in enumerate(arr):
            if len(l) == 0 or x >= l[-1]:
                l.append(x)
            else:
                break
        for i, x in enumerate(arr[::-1]):
            if len(r) == 0 or x <= r[0]:
                r.appendleft(x)
            else:
                break
        if len(l) == len(arr):
            return 0
        a, b = len(l), len(r)
        ans = b
        for i, x in enumerate(l):
            idx = bisect.bisect_left(r, x)
            ans = max(ans, i + 1 + b - idx)
        
        return len(arr) - ans

