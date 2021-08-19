class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        j = len(A)
        i = 0
        num = sum(A) // 3
        print(num)
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(0, j):
            sum1 = sum1 + A[i]
            i = i + 1
            if sum1 == num:
                break
        for i in range(i, j):
            sum2 = sum2 + A[i]
            i = i + 1
            if sum2 == num:
                break
        if i == j:
            return False
        sum3 = sum(A[i:])
        return sum1 == sum2 and sum1 == sum3
