class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        count = collections.defaultdict(int)
        min_heap = []
        max_heap = []
        ans = []
        max_length = 0

        for num in nums:
            ans.append(num)
            count[num] += 1
            if count[num] == 1:
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, num * -1)
            max_val = abs(max_heap[0])
            min_val = min_heap[0]
            while max_val - min_val > limit:
                popped_val = ans.pop(0)
                count[popped_val] -= 1
                # print(count)
                # print(min_heap)
                # print(ans)
                # print(min_val)
                # print(max_val)
                # Pop min_heap until you have a valid min_val
                if popped_val == min_val and count[popped_val] == 0:
                    while count[min_val] == 0:
                        heapq.heappop(min_heap)
                        min_val = min_heap[0]
                # Pop max_heap until you have a valid max_val
                if popped_val == max_val and count[popped_val] == 0:
                    while count[max_val] == 0:
                        heapq.heappop(max_heap)
                        max_val = abs(max_heap[0])

            max_length = max(max_length, len(ans))
        return max_length
