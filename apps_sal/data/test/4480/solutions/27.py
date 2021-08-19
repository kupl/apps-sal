class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        equalSum = sum(A) // 3
        part = 0
        numparts = 0
        r = sum(A) % 3
        for i in A:
            part += i
            if part == equalSum:
                part = 0
                numparts += 1
        return not r and numparts >= 3
