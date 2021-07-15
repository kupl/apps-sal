class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        S = sum(A)
        if S % 3 != 0:
            return False
        
        S_1 = S / 3
        S_2 = S_1 + S_1
        cur = A[0]
        for i in range(1, len(A)-2):
            if cur == S_1:
                cur += A[i]
                for j in range(i+1, len(A)-1):
                    if cur == S_2:
                        return True
                    else:
                        cur += A[j]
                
                if cur == S_2:
                    return A[-1] == S_1
            else:
                cur += A[i]

        if cur == S_1:
            return A[-1] == S_1

        return False
