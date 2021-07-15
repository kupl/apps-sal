class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        cusum = 0
        cusum_list = list()
        for i in range(len(A)):
            cusum += A[i]
            cusum_list.append(cusum)
        if sum(A)/3 in cusum_list:
            if sum(A)*2/3 in cusum_list[cusum_list.index(sum(A)/3) + 1:-1]:
                return True
            else:
                return False
        else:
            return False

