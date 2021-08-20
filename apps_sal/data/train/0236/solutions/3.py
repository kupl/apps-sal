class Solution:

    def minFlipsMonoIncr(self, S: str) -> int:
        str_len = len(S)
        count_arr = [[0, 0] for x in range(str_len)]
        one_start_idx = -1
        for i in range(len(S)):
            if S[i] == '0':
                if i == 0:
                    count_arr[i][0] += 1
                    count_arr[i][1] = 0
                else:
                    count_arr[i][0] = count_arr[i - 1][0] + 1
                    count_arr[i][1] = count_arr[i - 1][1]
            else:
                if i == 0:
                    count_arr[i][1] += 1
                else:
                    count_arr[i][1] = count_arr[i - 1][1] + 1
                    count_arr[i][0] = count_arr[i - 1][0]
                if one_start_idx == -1:
                    one_start_idx = i
        total_flips = []
        total_flips.append(min(count_arr[str_len - 1][0], count_arr[str_len - 1][1]))
        for i in range(one_start_idx, str_len):
            if i == 0:
                total_flips.append(count_arr[str_len - 1][0] - count_arr[i][0])
            elif i == str_len - 1:
                total_flips.append(count_arr[str_len - 1][0])
            else:
                total_flips.append(count_arr[i - 1][1] + count_arr[str_len - 1][0] - count_arr[i][0])
        return min(total_flips)
