class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        len_to_start = collections.defaultdict(list)
        (start, end) = (0, 1)
        tmp_sum = arr[0]
        (earliest_end, latest_start) = (len(arr), 0)
        while start < len(arr):
            while end < len(arr) and tmp_sum < target:
                tmp_sum += arr[end]
                end += 1
            if tmp_sum == target:
                len_to_start[end - start].append(start)
                earliest_end = min(earliest_end, end)
                latest_start = max(latest_start, start)
            tmp_sum -= arr[start]
            start += 1
        if earliest_end > latest_start:
            return -1
        for (l, starts) in list(len_to_start.items()):
            if len(starts) > 2:
                len_to_start[l] = [starts[0], starts[-1]]
        shortest = len(arr)
        for l1 in len_to_start:
            for s1 in len_to_start[l1]:
                for l2 in len_to_start:
                    for s2 in len_to_start[l2]:
                        if l1 + l2 >= shortest:
                            continue
                        if s1 < s2 and s1 + l1 <= s2:
                            shortest = l1 + l2
                        if s2 < s1 and s2 + l2 <= s1:
                            shortest = l1 + l2
        return shortest
