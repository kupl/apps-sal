import heapq


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        idea 1: sliding window:
                   r      
        [2, -1, 2, 3] 4
             l. 
        if cur_sum > k -> move l otherwise move r

        longest?
        [0, 2, -3, 5]   5
        '''
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        '''
        heapq[1, 2, 3]
        
        '''

        heap = []
        min_l = len(A) + 1
        for i, num in enumerate(P):
            while heap and num - heap[0][0] >= K:
                v, idx = heapq.heappop(heap)
                min_l = min(min_l, i - idx)
            heapq.heappush(heap, (num, i))
        return min_l if min_l < len(A) + 1 else -1
