class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        isUsed = dict()
        for i in range(len(s)):
            (ch1, ch2) = (ord(s[i]), ord(t[i]))
            if ch1 < ch2:
                shift = ch2 - ch1
            elif ch1 > ch2:
                shift = 26 - (ch1 - ch2)
            else:
                continue
            initShift = shift
            while 1 <= shift <= k:
                if shift not in isUsed:
                    isUsed[initShift] = shift
                    break
                shift = isUsed[initShift] + 26
            else:
                return False
        return True
