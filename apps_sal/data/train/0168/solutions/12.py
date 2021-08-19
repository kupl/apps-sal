class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        if k == len(s):
            return True
        charCount = Counter(s)
        countOdd = 0
        for count in list(charCount.values()):
            if count % 2 != 0:
                countOdd += 1
        return countOdd <= k
