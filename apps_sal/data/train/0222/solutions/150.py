class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        '''  
        dp = {i:[[A[i]]] for i in range(len(A))}
        res = 0
        for i in range(1, len(A)):
            for j in range(i):
                for sequence in dp[j]:
                    if len(sequence) <= 1 or\\
                        sequence[-2]==A[i]-sequence[-1]:
                        dp[i] += [sequence+[A[i]]]
                        if len(dp[i][-1]) >= 3:
                            res = max(res, len(dp[i][-1]))
        return res
        '''
        dp = {}
        for i in range(len(A)):
            b = A[i]
            for j in range(i):
                a = A[j]
                if (b - a, a) not in dp:
                    dp[(a, b)] = 2
                elif b - a < a:
                    dp[(a, b)] = dp[(b - a, a)] + 1
        res = max(dp.values())
        return res if res != 2 else 0
