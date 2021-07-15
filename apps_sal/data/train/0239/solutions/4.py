class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
#         # maintain max heap, get largest value for each label
#         # this brute force solution is O(nlogn + num_wanted)
#         values_by_label = defaultdict(list)
#         for i, val in enumerate(values):
#                 heapq.heappush(values_by_label[labels[i]], -1 * val)
        
#         total = 0
#         label_use_limit = defaultdict(int)
#         for label in values_by_label.keys():
#             label_use_limit[label] = use_limit

            
#         for _ in range(num_wanted - 1, -1, -1):
#             max_num = -1
#             for k, v in values_by_label.items():
#                 if label_use_limit[k] > 0 and len(v) > 0 and -1 * v[0] > max_num:
#                     max_num = -1 * v[0]
#                     best_label = k  
#             if max_num != -1:
#                 total += max_num
#                 heapq.heappop(values_by_label[best_label])
#                 label_use_limit[best_label] -= 1
        
#         return total

        ordered_values = [] # maxheap
        label_use_limit = defaultdict(int)
        for i, val in enumerate(values):
            heapq.heappush(ordered_values, (-1 * val, labels[i]))
            if labels[i] not in label_use_limit:
                label_use_limit[labels[i]] = use_limit
        total = 0
        while len(ordered_values) > 0 and num_wanted > 0:
            top_elem = heapq.heappop(ordered_values)
            if label_use_limit[top_elem[1]] > 0:
                total += (-1 * top_elem[0])
                label_use_limit[top_elem[1]] -= 1
                num_wanted -= 1
        return total

