class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:

        ordered_values = []
        label_use_limit = defaultdict(int)
        for i, val in enumerate(values):
            heapq.heappush(ordered_values, (-1 * val, labels[i]))
            if labels[i] not in label_use_limit:
                label_use_limit[labels[i]] = use_limit
        total = 0
        while len(ordered_values) > 0 and num_wanted > 0:
            top_elem = heapq.heappop(ordered_values)
            if label_use_limit[top_elem[1]] > 0:
                total += (-1 * top_elem[0])
                label_use_limit[top_elem[1]] -= 1
                num_wanted -= 1
        return total
