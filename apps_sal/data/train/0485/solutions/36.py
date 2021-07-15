class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res = 0
        queue = collections.deque([])
        
        for i in range(len(A)):
            while queue and queue[0] < i:
                queue.popleft()
            
            if (A[i] + len(queue)) % 2 == 0:
                if i+K-1 >= len(A):
                    return -1
                else:
                    queue.append(i+K-1)
                    res += 1
                    
        return res
