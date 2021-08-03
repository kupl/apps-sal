from queue import PriorityQueue


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        pq = PriorityQueue()
        for i in range(len(values)):
            pq.put((-values[i], labels[i]))

        subset_sum = 0
        ecount = 0
        label_usage_count_map = {}

        while (pq.qsize() > 0):
            popped_element = pq.get()
            v = -popped_element[0]
            l = popped_element[1]

            if (v < 0):
                break

            if (ecount >= num_wanted):
                break

            lusage = label_usage_count_map.get(l, 0)
            if (lusage >= use_limit):
                continue

            ecount += 1
            subset_sum += v
            label_usage_count_map[l] = label_usage_count_map.get(l, 0) + 1

        return subset_sum
