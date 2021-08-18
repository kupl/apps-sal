class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        count = [0 for _ in range(26)]
        for a, b in zip(s, t):
            if a == b:
                continue
            shift = (ord(b) - ord(a)) % 26
            count[shift] += 1
        max_shift = 0
        max_count = 0
        for i in range(25, -1, -1):
            if count[i] > max_count:
                max_shift = i
                max_count = count[i]
        if max_count < 1:
            return True
        return (((max_count - 1) * 26) + max_shift) <= k
