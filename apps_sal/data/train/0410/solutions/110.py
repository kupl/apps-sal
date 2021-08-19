import heapq


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:

        def power(num, cou=0):
            if num == 1:
                return cou
            if num % 2 == 0:
                num = num // 2
                return power(num, cou + 1)
            else:
                num = 3 * num + 1
                return power(num, cou + 1)
        arr = []
        while lo <= hi:
            j = power(lo)
            heapq.heappush(arr, (-j, -lo))
            if len(arr) > k:
                heapq.heappop(arr)
            lo += 1
        return -heapq.heappop(arr)[1]
