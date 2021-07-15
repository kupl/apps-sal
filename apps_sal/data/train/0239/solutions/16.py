from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        if not values or not labels:
            return 0
        index = [i for i in range(len(values))]
        index.sort(key=lambda i: values[i], reverse=True)
        res = 0
        lab_to_count = defaultdict(int)
        for i in index:
            if num_wanted == 0:
                return res
            l = labels[i]
            v = values[i]
            if l not in lab_to_count or lab_to_count[l] < use_limit:
                res += v
                lab_to_count[l] += 1
                num_wanted -= 1    
        return res

