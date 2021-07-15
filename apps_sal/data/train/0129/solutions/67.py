import heapq
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        return solution(A)

        
def solution(A):
    right_heap = [(-(a - i), a, i) for i, a in enumerate(A)]
    
    heapq.heapify(right_heap)
    current_max = -1    
    
    for i in range(len(A) - 1):
        right_max_score = -1
        while len(right_heap) > 0 and right_heap[0][2] <= i:
            heapq.heappop(right_heap)
        el = right_heap[0]

        right_max_score = A[i] + el[1] - abs(el[2] - i)
        current_max = max(right_max_score, current_max)

    return current_max
