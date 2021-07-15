
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = sorted(zip(speed, efficiency), key=lambda x: x[1],reverse=True)
        
        result, sum_speed = 0, 0
        min_heap = []
        print(people)
        for i, (s, e) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)
                
            result = max(result, sum_speed * e)
            print(result)
        
        return result % (pow(10,9)+7)

