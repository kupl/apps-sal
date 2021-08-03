class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        presum = [0]
        for x in A:
            # if x>=K: return 1, faster without this one
            presum.append(presum[-1] + x)

        q = collections.deque()
        ans = math.inf
        for i, x in enumerate(A):
            while q and presum[i + 1] - presum[q[-1]] <= x:
                q.pop()
            q.append(i)
            while q and (presum[i + 1] - presum[q[0]] >= K):  # or i+1-q[0]>=ans:
                ans = min(ans, i + 1 - q[0])
                q.popleft()
        return ans if ans != math.inf else -1
