class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        heap_nums = []
        groups = []
        for key, val in counter.items():
            heapq.heappush(heap_nums, (key, val))

        while(heap_nums):
            count = 0
            sub_group = []
            remaining_elements = []
            while(count < k):
                if not heap_nums:
                    return False
                popped_elem = heapq.heappop(heap_nums)
                if popped_elem[1] - 1 > 0:
                    remaining_elements.append(popped_elem)
                if not sub_group:
                    sub_group.append(popped_elem[0])
                else:
                    if popped_elem[0] - 1 == sub_group[-1]:
                        sub_group.append(popped_elem[0])
                    else:
                        return False
                count += 1

            groups += sub_group
            for elem in remaining_elements:
                heapq.heappush(heap_nums, (elem[0], elem[1] - 1))

        return True
