class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tot_sum = sum(A)
        if tot_sum % 3 != 0:
            return(False)
        else:
            cum_sum = 0
            target = tot_sum // 3
            counter = 0
            for num in A[:-1]:
                cum_sum += num
                if cum_sum == target:
                    counter += 1
                    cum_sum = 0
                    if counter == 2:
                        return(True)
            return(False)
