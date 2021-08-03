from collections import Counter
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        count_num = []
        for num, count in freq.items():
            count_num.append((count, num))
        heapq.heapify(count_num)
        print(count_num)
        while k > 0:
            count, num = heapq.heappop(count_num)
            k -= count
        if k == 0:
            return len(count_num)
        elif k < 0:
            return len(count_num) + 1
