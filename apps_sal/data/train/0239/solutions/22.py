from collections import Counter
import heapq


class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        h = list(zip([-v for v in values], labels))
        heapq.heapify(h)
        counter = Counter()
        ans = 0
        while num_wanted and h:
            heap_item = heapq.heappop(h)
            (val, label) = heap_item
            if counter[label] == use_limit:
                continue
            counter[label] += 1
            ans += -val
            num_wanted -= 1
        return ans
