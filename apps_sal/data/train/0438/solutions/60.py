class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr_len = len(arr)
        d = {i: [i - 1, 0, i + 1] for i in range(arr_len + 1)}
        last_round = -1
        count_m = 0
        for (cur_round, n) in enumerate(arr):
            (prev_idx, this_len, next_idx) = d[n]
            if this_len == m:
                count_m -= 1
            if d[prev_idx][1] == m:
                count_m -= 1
            new_len = d[prev_idx][1] + this_len + 1
            d[prev_idx][1] = new_len
            d[prev_idx][2] = next_idx
            if next_idx <= arr_len:
                d[next_idx][0] = prev_idx
            d[n] = None
            if new_len == m:
                count_m += 1
            if count_m > 0:
                last_round = cur_round + 1
        return last_round
