class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        substring_set = set()
        need = 1 << k
        for start in range(len(s) - k + 1):
            ss = s[start:start + k]
            if ss not in substring_set:
                substring_set.add(ss)
                need -= 1
                if need == 0:
                    return True

        return False
