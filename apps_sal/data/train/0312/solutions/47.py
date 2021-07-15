import collections

class Solution:
    def shortestSubarray(self, A, K):
        d = collections.deque()
        cummulative_sum = [0]
        
        for a in A:
            cummulative_sum.append(cummulative_sum[-1] + a)
        
        ans = len(cummulative_sum)

        for idx, x in enumerate(cummulative_sum):
            while d and x <= cummulative_sum[d[-1]]:
                d.pop()
            
            while d and x - cummulative_sum[d[0]] >= K:
                ans = min(ans, idx - d[0])
                d.popleft()
            
            d.append(idx)
        
        return ans if ans != len(cummulative_sum) else -1
