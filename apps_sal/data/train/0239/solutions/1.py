class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        val_label = list(sorted(zip(values, labels), key=lambda x: x[0], reverse=True))
        cnt_label = collections.Counter()
        chosen = 0
        res = 0
        for (val, lab) in val_label:
            if chosen < num_wanted:
                if cnt_label[lab] < use_limit:
                    res += val
                    chosen += 1
                    cnt_label[lab] += 1
        return res
