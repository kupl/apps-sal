class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        min_range = None
        left = self.get_list(arr, target)
        right = list(reversed(self.get_list(list(reversed(arr)), target)))
        print(left)
        print(right)
        min_length = None
        for i in range(len(arr) - 1):
            if left[i] != -1 and right[i + 1] != -1:
                if not min_length:
                    min_length = left[i] + right[i + 1]
                else:
                    min_length = min(left[i] + right[i + 1], min_length)
        return -1 if not min_length else min_length

    def get_list(self, arr, target):
        prefix_d = dict()
        prefix_d[0] = -1
        min_range_list = []
        current_min = -1
        current = 0
        for i in range(len(arr)):
            current += arr[i]
            if current - target in prefix_d:
                prev_idx = prefix_d[current - target]
                dis = i - prev_idx
                if current_min == -1:
                    current_min = dis
                else:
                    current_min = min(current_min, dis)
            min_range_list.append(current_min)
            prefix_d[current] = i
        return min_range_list
