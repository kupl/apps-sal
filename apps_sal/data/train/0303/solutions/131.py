class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        d = [0] * (1 + len(arr) + k)
        for ind in range(1, len(arr) + 1):
            for sub_arr_st in range(min(ind, k)):
                if arr[ind - sub_arr_st - 1] > arr[ind - 1]:
                    break
                for sub_arr_len in range(sub_arr_st + 1, k + 1):
                    ind_x = ind - sub_arr_st + sub_arr_len - 1
                    d[ind_x] = max(d[ind_x], d[ind - sub_arr_st - 1] + arr[ind - 1] * sub_arr_len)
        return d[len(arr)]
