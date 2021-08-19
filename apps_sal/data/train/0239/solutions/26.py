class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        val_label_tuple = [(-1 * val, lab) for (val, lab) in zip(values, labels)]
        import heapq
        heapq.heapify(val_label_tuple)
        counts = collections.defaultdict(int)
        ans = 0
        while val_label_tuple:
            (val, lab) = heapq.heappop(val_label_tuple)
            if counts.get(lab, 0) < use_limit:
                ans += abs(val)
                num_wanted -= 1
                if num_wanted == 0:
                    break
                counts[lab] += 1
        return ans
        '\n        val_label_tuple = [(val, lab) for val, lab in zip(values, labels)]\n        val_label_tuple = sorted(val_label_tuple, key=lambda x: x[0], reverse=True)\n        \n        count_items = defaultdict(int)\n        ret_value = 0\n        \n        for val, label in val_label_tuple:\n            if count_items.get(label, 0) < use_limit:\n                ret_value += val\n                count_items[label] += 1\n                num_wanted -= 1\n                if num_wanted == 0:\n                    break\n        \n        return ret_value\n        '
