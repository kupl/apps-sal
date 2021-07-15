from functools import lru_cache 
class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        @lru_cache(maxsize = None)
        def findMaxReach(index):
            best = 1
            for i in range(1, d + 1):
                curIndex = index - i
                if 0 <= curIndex < n and arr[curIndex] < arr[index]:
                    best = max(findMaxReach(curIndex) + 1, best)
                else:
                    break
            for i in range(1, d + 1):
                curIndex = index + i
                if 0 <= curIndex < n and arr[curIndex] < arr[index]:
                    best = max(findMaxReach(curIndex) + 1, best)
                else:
                    break
            return best
        ans = 0
        for i in range(n):
            ans = max(findMaxReach(i), ans)
        return ans

