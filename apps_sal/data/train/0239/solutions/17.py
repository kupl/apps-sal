class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        all_value_labels = [(value, label) for value, label in zip(values, labels)]
        all_value_labels.sort(reverse=True)
        used = Counter()
        ans = []
        for value, label in all_value_labels:
            if used[label] + 1 <= use_limit:
                used[label] += 1
                ans.append(value)
                if len(ans) == num_wanted:
                    break
        return sum(ans)

