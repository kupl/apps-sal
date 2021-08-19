class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        cummulative_sum = 0
        counter = 0
        target = sum(A) / 3
        if target != int(target):
            return False
        print(target)
        for idx in range(len(A)):
            cummulative_sum += A[idx]
            if cummulative_sum == target:
                cummulative_sum = 0
                counter += 1
        if counter == 4 and target == 0:
            return True
        if counter == 3:
            return True
        return False
