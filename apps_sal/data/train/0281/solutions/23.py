class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        seen = set()

        for cs, ct in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26
            if diff != 0:
                if diff in seen:
                    count[diff] += 26
                    if count[diff] > k:
                        return False
                else:
                    count[diff] = diff
                    if diff > k:
                        return False
                    seen.add(diff)
        return True
