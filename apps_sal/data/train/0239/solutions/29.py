from heapq import *


class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        maxHeap = []
        maxSum = 0
        for i in range(len(values)):
            heappush(maxHeap, (-values[i], labels[i]))
        usedLabels = defaultdict(int)
        while num_wanted > 0 and len(maxHeap) > 0:
            (currVal, currLabel) = heappop(maxHeap)
            if usedLabels[currLabel] < use_limit:
                usedLabels[currLabel] += 1
                maxSum -= currVal
                num_wanted -= 1
        return maxSum
