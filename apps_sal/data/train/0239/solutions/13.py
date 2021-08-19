from collections import defaultdict


class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        if len(values) == 0:
            return 0
        if len(values) != len(labels):
            raise ValueError
        sorted_value_labels = sorted(zip(values, labels), key=lambda x: -x[0])
        label_counter = defaultdict(lambda: 0)
        i = 0
        total = 0
        S = 0
        while S != num_wanted and i < len(values):
            (val, label) = sorted_value_labels[i]
            if label_counter[label] < use_limit:
                total += val
                label_counter[label] += 1
                S += 1
            i += 1
        return total
