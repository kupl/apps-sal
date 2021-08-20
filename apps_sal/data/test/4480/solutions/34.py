class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        flag = 0
        temp = 0
        for i in range(len(A)):
            temp += A[i]
            if flag == 0 and temp == s // 3:
                flag += 1
            elif flag == 1 and temp == s * 2 / 3 and (i != len(A) - 1):
                return True
        return False
