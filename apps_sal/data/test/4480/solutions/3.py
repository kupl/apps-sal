class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for i in A:
            sum += i
        s = 0
        c = 0
        for i in A:
            s += i
            if s == int(sum / 3):
                s = 0
                c += 1
        return c >= 3
