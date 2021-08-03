class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if len(nums) % k != 0:
            return False

        counter = Counter(nums)
        heap = []

        for num in counter:
            heapq.heappush(heap, (num, counter[num]))

        while len(heap) >= k:
            i = 0
            temp = []
            prevNum = None
            for i in range(k):
                num, count = heapq.heappop(heap)
                if not prevNum:
                    prevNum = num

                else:
                    if prevNum + 1 != num:
                        return False
                    prevNum = num

                count -= 1
                if count > 0:
                    temp.append((num, count))

            for n, count in temp:
                heapq.heappush(heap, (n, count))

        print(heap)
        return len(heap) == 0
