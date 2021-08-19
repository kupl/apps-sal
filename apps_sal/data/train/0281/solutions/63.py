def no_of_shifts_away(a, b):
    return (ord(b) - ord(a)) % 26


class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        in1_len = len(s)
        freq = {}
        in2_len = len(t)
        max_duplicates_in_shift = []
        for i in range(26):
            max_duplicates_in_shift.append(max(0, 1 + (k - i) // 26))
        if in1_len != in2_len:
            return False
        for i in range(in1_len):
            shifts_required = no_of_shifts_away(s[i], t[i])
            if shifts_required > k:
                return False
            if shifts_required != 0:
                if shifts_required in freq:
                    freq[shifts_required] += 1
                    if freq[shifts_required] > max_duplicates_in_shift[shifts_required]:
                        return False
                else:
                    freq[shifts_required] = 1
        return True
