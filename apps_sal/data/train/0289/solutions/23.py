class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
        O(n^2)
        '''

        long = L if L > M else M
        short = M if M < L else L

        global_max = 0
        for i in range(0, len(A) - long + 1):
            temp1 = sum(A[i:i + long])
            left = A[:i]
            right = A[i + long:]
            if len(left) >= short:
                for j in range(0, len(left) - short + 1):
                    temp2 = sum(left[j:j + short])
                    if temp1 + temp2 > global_max:
                        global_max = temp1 + temp2
            if len(right) >= short:
                for j in range(0, len(right) - short + 1):
                    temp2 = sum(right[j:j + short])
                    if temp1 + temp2 > global_max:
                        global_max = temp1 + temp2

        return global_max
