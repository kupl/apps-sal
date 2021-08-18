from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        diff_to_longer_len = defaultdict(int)
        diff_to_longer_len[0] = 0

        def replace_if_larger(dct, key, val):
            dct[key] = max(val, dct[key])

        for new_L in rods:
            tmp = defaultdict(int)
            for dL, L in list(diff_to_longer_len.items()):
                replace_if_larger(tmp, new_L + dL, new_L + L)
                replace_if_larger(tmp, abs(new_L - dL), max(L, new_L + L - dL))

            for dL, L in list(tmp.items()):
                replace_if_larger(diff_to_longer_len, dL, L)

        return diff_to_longer_len[0]
