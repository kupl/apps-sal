from typing import *


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return longestCommonSubsequence_DP(text1, text2, 0, 0, dict())


def longestCommonSubsequence_DP(text1: str, text2: str, first_start_idx: int, second_start_idx: int, memo: Dict):
    if (first_start_idx, second_start_idx) in memo:
        return memo[(first_start_idx, second_start_idx)]

    # base cases
    if first_start_idx == len(text1) or second_start_idx == len(text2):
        return 0

    # recursive cases
    first_cur_char = text1[first_start_idx]
    second_cur_char = text2[second_start_idx]
    ans_if_cur_same = -1
    if first_cur_char == second_cur_char:
        ans_if_cur_same = 1 + longestCommonSubsequence_DP(text1, text2, first_start_idx + 1, second_start_idx + 1, memo)

    ans1_if_cur_diff = longestCommonSubsequence_DP(text1, text2, first_start_idx, second_start_idx + 1, memo)
    ans2_if_cur_diff = longestCommonSubsequence_DP(text1, text2, first_start_idx + 1, second_start_idx, memo)

    memo[(first_start_idx, second_start_idx)] = max(ans_if_cur_same if ans_if_cur_same != -1 else -math.inf,
                                                    ans1_if_cur_diff,
                                                    ans2_if_cur_diff)
    return memo[(first_start_idx, second_start_idx)]
