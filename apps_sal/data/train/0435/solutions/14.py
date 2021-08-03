class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        su = 0
        dic = {}
        count = 0
        for i in range(len(A)):

            su += A[i]

            if(su % K == 0):
                count += 1
            if((su) % K in dic.keys()):
                count += dic[(su) % K]

            if(su % K in dic.keys()):
                dic[su % K] += 1
            else:
                dic[su % K] = 1
        print(dic)
        print(count)
        return count
