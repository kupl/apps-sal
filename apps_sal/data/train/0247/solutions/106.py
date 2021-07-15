class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        p = [0]
        m = {0: -1}
        minLen = [float('inf')]
        cur = 0
        ans = best = float('inf')
        for i, a in enumerate(arr):
            cur += a
            p.append(cur)
            if cur-target in m:
                ans = min(ans, i-m[cur-target]+minLen[m[cur-target]+1])
                best = min(i-m[cur-target], best)
            minLen.append(best)
            m[cur] = i
        
        return ans if ans != float('inf') else -1
