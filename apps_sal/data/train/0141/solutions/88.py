class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        heap = []
        people.sort()
        heap.append((people[len(people) - 1], 1))
        i = len(people) - 2
        while i >= 0:
            ele = people[i]
            if limit >= ele + heap[0][0] and heap[0][1] < 2:
                minimum = heapq.heappop(heap)
                heapq.heappush(heap, (float('inf'), 2))
            else:
                heapq.heappush(heap, (ele, 1))
            i -= 1
        print(heap)
        return len(heap)
