class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        sCounter = collections.Counter(s)
        numberOfLettersWithOddCounts = len([count for count in list(sCounter.values()) if count % 2 != 0])
        return not (len(s) < k or numberOfLettersWithOddCounts > k)
