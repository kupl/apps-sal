import heapq


class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        maxHeap = []
        for (value, label) in zip(values, labels):
            print((value, label))
            heappush(maxHeap, (-value, label))
        labelFrequencies = {}
        maxSum = 0
        numChosen = 0
        while maxHeap and numChosen < num_wanted:
            (value, label) = heappop(maxHeap)
            value = -value
            if label in labelFrequencies and labelFrequencies[label] >= use_limit:
                continue
            if label not in labelFrequencies:
                labelFrequencies[label] = 0
            labelFrequencies[label] += 1
            numChosen += 1
            maxSum += value
        return maxSum
