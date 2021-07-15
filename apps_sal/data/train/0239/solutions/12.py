class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heap = []
        for v, l in zip(values, labels):
            heapq.heappush(heap, (-v, l))
        
        count = collections.Counter()
        res = []
        while heap and len(res) < num_wanted:
            v, l = heapq.heappop(heap)
            if count[l] < use_limit:
                res.append(v)
                count[l] += 1
        return -sum(res)
        

