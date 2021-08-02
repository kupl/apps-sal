class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        j = len(A)
        i = 0
        num = 0
        for i in range(0, j):
            num = num + A[i]
        num = floor(num / 3)
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
        for i in range(i, j):
            sum3 = sum3 + A[i]
            i = i + 1
            if sum3 == num:
                break
        print(sum1)
        return sum1 == sum2 and sum1 == sum3

        # return sum3
#         for i in range(0, floor(j/3)):
#             sum1 = sum1 + A[i]
#             i = i+1

#         sum2 =0
#         print(\"sum1 = \" , sum1)
#         while sum2 is not sum1:
#             sum2 = sum2 + A[i]
#             print(sum2)
#             i= i+1

#         sum3 =0
#         for i in range(i,j):
#             sum3 = sum3 +A[i]
#             # print(sum3)
