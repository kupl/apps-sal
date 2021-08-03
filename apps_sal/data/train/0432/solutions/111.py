class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        count = collections.Counter(nums)

        heap = []
        for (num, cnt) in count.items():
            heapq.heappush(heap, (num, cnt))

        while heap:
            nums, cnts = [], []
            for _ in range(k):
                if not heap:
                    return False
                else:
                    (num, cnt) = heapq.heappop(heap)
                    nums.append(num)
                    cnts.append(cnt)

            if not all(b == a + 1 for (a, b) in zip(nums, nums[1:])):
                return False

            for (num, cnt) in zip(nums, cnts):
                if cnt > 1:
                    heapq.heappush(heap, (num, cnt - 1))

        return True
