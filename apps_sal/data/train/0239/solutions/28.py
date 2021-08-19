class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        values_w_labels = [(values[i], labels[i]) for i in range(len(values))]
        values_w_labels.sort(reverse=True)
        label_count = {}
        total = 0
        count = 0
        for (value, label) in values_w_labels:
            if label not in label_count:
                label_count[label] = 0
            if label_count[label] < use_limit:
                total += value
                label_count[label] += 1
                count += 1
            if count == num_wanted:
                break
        return total
