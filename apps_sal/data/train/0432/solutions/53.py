from queue import PriorityQueue


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if len(nums) % k != 0:
            return False

        d = {}
        heap = PriorityQueue()
        for i in nums:

            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
                heap.put(i)

        i = 0

        while(i < len(nums)):

            min_val = heap.get()
            d[min_val] -= 1
            for j in range(1, k):

                if d.get(min_val + j):
                    heap.get()
                    d[min_val + j] -= 1
                else:
                    return False

            for j in range(0, k):
                if d.get(min_val + j) > 0:

                    heap.put(min_val + j)

            i += k

        return True
