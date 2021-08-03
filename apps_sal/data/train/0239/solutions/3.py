class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        res = 0
        heap = [[-v, i] for v, i in zip(values, labels)]
        heapq.heapify(heap)
        counter = Counter()

        while heap and num_wanted:
            v, i = heapq.heappop(heap)
            if counter[i] == use_limit:
                continue

            counter[i] += 1
            res += -v
            num_wanted -= 1

        return res
