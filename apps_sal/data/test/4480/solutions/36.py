
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        total = sum(A)
        curr_sum = 0
        first_found_flag = False

        for i in range(len(A) - 1):
            curr_sum += A[i]
            if not first_found_flag:
                if curr_sum == total / 3:
                    first_found_flag = True
            else:
                if curr_sum == total * 2 / 3:
                    return True

        return False
