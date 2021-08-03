class Solution:
    def maxPerformance1(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        total, sumSpeed = 0, 0
        for s, e in people:
            sumSpeed += s
            total = max(total, sumSpeed * e)
        return total

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        print(people)
        result, sum_speed = 0, 0
        min_heap = []
        for i, (s, e) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)

            result = max(result, sum_speed * e)

        return result % 1000000007
