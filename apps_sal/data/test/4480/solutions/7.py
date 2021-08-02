class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        required_sum = sum(A) // 3
        count_partition = 0
        curr_sum = A[0]
        i = 1
        while i < len(A):
            while i < len(A) and curr_sum != required_sum:
                curr_sum += A[i]
                i += 1
            if curr_sum == required_sum:
                count_partition += 1
                if i < len(A):
                    curr_sum = A[i]
                    i += 1
                    if i == len(A) and curr_sum == required_sum:
                        count_partition += 1
        if count_partition > 3 and required_sum == 0:
            count_partition = 3
        return count_partition == 3
