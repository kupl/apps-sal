class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # a + ....+ b = num
        # if 3 equal amount of indices have the same sum  return true
        # how do we find the sum?
        # use the sum and then divide it by three thats the equal part sum
        # use len(A) - 1  to find the number of indexes and
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
