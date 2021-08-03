class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sum1 = sum(A)
        count1 = 0
        dict1 = {0: 1}
        rem1 = 0
        sum2 = 0
        for i in range(len(A)):
            sum2 += A[i]
            rem1 = sum2 % K
            if rem1 < 0:
                rem1 += k

            if rem1 in dict1:
                count1 += dict1[rem1]
                dict1[rem1] += 1

            else:
                dict1[rem1] = 1
        print(dict1)
        return count1
