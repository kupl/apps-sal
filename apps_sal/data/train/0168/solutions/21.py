class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        dict = {}
        for st in s:
            if st in dict:
                dict[st] += 1
            else:
                dict[st] = 1

        countOddCh = 0
        for key, v in dict.items():
            if v % 2 != 0:
                countOddCh += 1

        if countOddCh > k:
            return False

        return True
