from collections import defaultdict
from queue import PriorityQueue


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        q = PriorityQueue()
        for i in range(len(values)):
            q.put((-values[i], values[i], labels[i]))
        d = defaultdict(lambda: 0)
        ans = []
        while len(ans) < num_wanted and not q.empty():
            _, n, l = q.get()
            if d[l] < use_limit:
                ans.append(n)
                d[l] += 1
        return sum(ans)
