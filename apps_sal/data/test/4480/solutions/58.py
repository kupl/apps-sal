class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        sum_a = sum(A)
        if sum_a % 3 != 0:
            return False
        target = sum_a // 3
        output = []
        temp_sum = 0
        temp_output = []
        for i in A:
            temp_output.append(i)
            temp_sum = temp_sum + i
            if temp_sum == target:
                if len(temp_output) > 0 and len(output) < 3:
                    output.append(temp_output)
                    temp_sum = 0
                    temp_output = []
        if temp_sum != 0:
            return False
        if len(output) != 3:
            return False
        else:
            return True
