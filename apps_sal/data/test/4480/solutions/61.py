class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if(sum(A) % 3 != 0):
            return False
        val = sum(A) // 3
        add = 0
        count = 0
        for x in range(len(A)):
            add += A[x]
            if(add == val):
                add = 0
                count += 1
            else:
                continue
        if(count >= 3):
            return True
        return False
