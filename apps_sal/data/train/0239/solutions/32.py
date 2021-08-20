class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        from heapq import heapify, heappop
        from collections import Counter
        counter = Counter()
        (pq, ans) = ([[-value, label] for (value, label) in zip(values, labels)], [])
        heapify(pq)
        while pq:
            cur = heappop(pq)
            if counter[cur[1]] < use_limit:
                counter[cur[1]] += 1
                ans.append(-cur[0])
                if len(ans) == num_wanted:
                    break
        return sum(ans)
