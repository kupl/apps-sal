class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        deq = collections.deque([])
        prefix = [0]
        res = float('inf')
        for a in A:
            prefix.append(prefix[-1] + a)
        for i, x in enumerate(prefix):
            while deq and prefix[deq[-1]] >= x:
                deq.pop()
            while deq and prefix[deq[0]] <= x - K:
                res = min(res, i - deq.popleft())
            deq.append(i)
        return res if res < float('inf') else -1       
