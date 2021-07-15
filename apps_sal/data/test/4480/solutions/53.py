class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tot = sum(A)
        if tot % 3 != 0:
            return False
        target = tot // 3
        curr_sum = 0
        check1, check2 = 0, 0
        for i, a in enumerate(A):
            curr_sum += a
            
            if check1 != 1 and curr_sum == target:
                check1 = 1
                continue
            # print(target, curr_sum)
            if check1 and curr_sum == target*2 and i < len(A) - 1:
                check2 = 1
                break
        if check1 and check2:
            return True
        else:
            return False

