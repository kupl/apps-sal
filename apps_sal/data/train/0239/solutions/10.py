class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        res = 0
        arr = sorted(list(zip(values, labels)), key=lambda x: x[0], reverse=1)
        cnt_label = {}
        cnt_tot = 0
        for val, lab in arr:
            if cnt_tot < num_wanted and cnt_label.get(lab, 0) < use_limit:
                cnt_tot += 1
                cnt_label[lab] = cnt_label.get(lab, 0) + 1
                res += val
        return res

