class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr_len = len(arr)
        d = {i: [i - 1, 0, i + 1] for i in range(arr_len + 1)}  # d[i] = (previous i, length ones start i)
        last_round = -1  # last round where we had string of length m
        count_m = 0  # count of current number of such strings

        for cur_round, n in enumerate(arr):
            prev_idx, this_len, next_idx = d[n]
            if this_len == m:
                count_m -= 1
            if d[prev_idx][1] == m:
                count_m -= 1
            new_len = d[prev_idx][1] + this_len + 1
            d[prev_idx][1] = new_len
            d[prev_idx][2] = next_idx

            if next_idx <= arr_len:  # only set if still in rang
                d[next_idx][0] = prev_idx

            d[n] = None   # so generate error if reuse

            if new_len == m:
                count_m += 1
            if count_m > 0:
                last_round = cur_round + 1
        return last_round
