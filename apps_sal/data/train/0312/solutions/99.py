class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        idea 1: sliding window:
                   r      
        [2, -1, 2, 3] 4
             l. 
        if cur_sum > k -> move l otherwise move r
        '''
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        # the largest i for j such that  A[j] - A[i] >= k
        # [2, -1, 2, 3]  -> [0, 2, 1, 3, 5]
        # [0, 1, 3, 5]
        #
        ans = len(A) + 1
        dq = collections.deque([])
        for i, y in enumerate(P):
            while dq and y < P[dq[-1]]:
                dq.pop()
            while dq and y - P[dq[0]] >= K:
                ans = min(ans, i - dq.popleft())
            dq.append(i)
        return ans if ans < len(A) + 1 else -1
