from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        counts = defaultdict(int)
        s = 0
        total_count = 0
        
        inds = sorted(list(range(len(values))), key=lambda x: values[x], reverse=True)
        
        sorted_values = [values[idx] for idx in inds]
        sorted_labels = [labels[idx] for idx in inds]
        
        for i, val in enumerate(sorted_values):
            label = sorted_labels[i]
            if total_count < num_wanted and counts[label] < use_limit:
                counts[label] += 1
                total_count += 1
                s += val
                
            if total_count == num_wanted:
                break
        return s

