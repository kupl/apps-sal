from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        diff_to_longer_len = defaultdict(int)
        diff_to_longer_len[0] = 0

        for new_L in rods:
            tmp = defaultdict(int)
            for delta_L, L in list(diff_to_longer_len.items()):
                tmp[delta_L + new_L] = max(
                    L + new_L,
                    tmp[delta_L + new_L],
                )
                tmp[abs(delta_L - new_L)] = max(
                    L,
                    L - delta_L + new_L,
                    tmp[abs(delta_L - new_L)],
                )

            for delta_L, L in list(tmp.items()):
                diff_to_longer_len[delta_L] = max(
                    L,
                    diff_to_longer_len[delta_L],
                )

        return diff_to_longer_len[0]
