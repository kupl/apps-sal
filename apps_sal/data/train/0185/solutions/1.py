class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2 ** k + k - 1:
            return False
        target = 2 ** k
        seen = set()
        cur_len = 0
        for end in range(k, len(s) + 1):
            chunk = s[end - k: end]
            if chunk not in seen:
                cur_len += 1
                seen.add(chunk)
                if cur_len == target:
                    return True
        return len(seen) == target
