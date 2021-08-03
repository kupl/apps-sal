class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        val_label_tuple = [(-1 * val, lab) for val, lab in zip(values, labels)]
        import heapq
        heapq.heapify(val_label_tuple)  # maximum val is at the top
        counts = collections.defaultdict(int)

        ans = 0
        while val_label_tuple:
            val, lab = heapq.heappop(val_label_tuple)
            if counts.get(lab, 0) < use_limit:
                ans += abs(val)
                num_wanted -= 1
                if num_wanted == 0:
                    break
                counts[lab] += 1

        return ans

        '''
        val_label_tuple = [(val, lab) for val, lab in zip(values, labels)]
        val_label_tuple = sorted(val_label_tuple, key=lambda x: x[0], reverse=True)
        
        count_items = defaultdict(int)
        ret_value = 0
        
        for val, label in val_label_tuple:
            if count_items.get(label, 0) < use_limit:
                ret_value += val
                count_items[label] += 1
                num_wanted -= 1
                if num_wanted == 0:
                    break
        
        return ret_value
        '''
