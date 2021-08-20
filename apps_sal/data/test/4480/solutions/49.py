class Solution:

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        for a in A:
            sum += a
        target = floor(sum / 3)
        sum = 0
        cnt = 0
        j = len(A) - 1
        i = 0
        while j > 0:
            sum += A[j]
            if sum == target:
                cnt += 1
                sum = 0
                break
            j -= 1
        while i < j:
            sum += A[i]
            if cnt < 2 and sum == target:
                cnt += 1
                sum = 0
                if j - i <= 1:
                    return False
            i += 1
            if i >= j:
                break
        if cnt == 2 and sum == target:
            cnt += 1
        if cnt == 3:
            return True
        return False
