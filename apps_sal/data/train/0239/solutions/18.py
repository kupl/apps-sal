class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        heap = []
        for i in range(len(values)):
            heappush(heap, (-values[i], labels[i]))
        (selected, label_counts) = ([], {})
        while len(selected) < num_wanted and heap:
            (value, label) = heappop(heap)
            if (cur_num := label_counts.get(label, 0)) < use_limit:
                label_counts[label] = cur_num + 1
                selected.append(value)
        print(selected)
        return -sum(selected)
