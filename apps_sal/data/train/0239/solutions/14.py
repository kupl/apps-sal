class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        sum = 0
        ct = {}
        import numpy as np
        sorted_idx = np.argsort(-np.array(values))
        select_ct = 0
        for v in sorted_idx:
            print(v)
            if select_ct == num_wanted:
                break
            label = labels[v]
            if label not in list(ct.keys()):
                ct[label] = 1
                sum += values[v]
                select_ct += 1
            elif ct[label] < use_limit:
                ct[label] += 1
                sum += values[v]
                select_ct += 1
            else:
                continue
            print(sum)
        return sum
        

