class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = collections.deque([(0, 0)])
        cur_sum = 0
        res = len(A) +1
        
        for right, val in enumerate(A):
            cur_sum += val
            while queue and cur_sum - queue[0][1] >= K:
                res = min(res, right+1-queue.popleft()[0])
            while queue and queue[-1][1] >= cur_sum:
                queue.pop()
                
            queue.append((right+1, cur_sum))
                
        if res <= len(A):
            return res
        return -1
