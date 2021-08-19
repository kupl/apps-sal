class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # for i in range(2**k):
        #     ss=(bin(i)[2::]).zfill(k)
        #     if ss not in s:
        #         return False
        # return True
        d = set()
        for i in range(len(s) - k + 1):
            if s[i:i + k] not in d:
                d.add(s[i:i + k])
                if len(d) == 2**k:
                    return True
        return False
