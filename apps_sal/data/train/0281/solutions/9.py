# 1540. Can Convert String in K Moves

ALPHABET_SIZE = 26

def compute_shift (c1, c2):
    return (ord (c2) - ord (c1)) % ALPHABET_SIZE

def last_shift (shift, frequency):
    return shift + (frequency - 1) * ALPHABET_SIZE

def can_convert_string (s, t, k):
    if len(s) != len(t): return False
    shifts = {}
    for c1, c2 in zip (s, t):
        if c1 != c2:
            shift = compute_shift (c1, c2)
            shifts.setdefault (shift, 0)
            shifts[shift] += 1

    return all (last_shift (shift, frequency) <= k for (shift, frequency) in shifts.items ())

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        return can_convert_string(s, t, k)
